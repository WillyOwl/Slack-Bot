import unittest
from unittest.mock import patch, MagicMock
import json
import os
import sys
import requests

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        # Create a mock for the API key
        with patch('utils.weather_api.WEATHER_API_KEY', 'mock_api_key'):
            self.weather_api = WeatherAPI()
    
    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'name': 'New York',
            'sys': {'country': 'US'},
            'weather': [{'description': 'clear sky', 'icon': '01d'}],
            'main': {'temp': 20.5, 'feels_like': 19.8, 'humidity': 65},
            'wind': {'speed': 3.6}
        }
        mock_get.return_value = mock_response
        
        # Call the method
        result = self.weather_api.get_weather('New York')
        
        # Assertions
        self.assertTrue(result['success'])
        self.assertEqual(result['data']['location'], 'New York')
        self.assertEqual(result['data']['country'], 'US')
        self.assertEqual(result['data']['description'], 'clear sky')
        self.assertEqual(result['data']['temperature'], 20.5)
        self.assertEqual(result['data']['humidity'], 65)
    
    def test_get_weather_request_error(self):
        # Use a context manager to patch requests.get
        with patch('requests.get') as mock_get:
            # Configure the mock to raise an exception
            mock_get.side_effect = requests.exceptions.RequestException("API error")
            
            # Call the method
            result = self.weather_api.get_weather('Invalid Location')
            
            # Assertions
            self.assertFalse(result['success'])
            self.assertTrue('Error fetching weather data' in result['error'])
    
    def test_format_weather_response_success(self):
        # Test data
        weather_data = {
            'success': True,
            'data': {
                'location': 'London',
                'country': 'GB',
                'description': 'light rain',
                'temperature': 15.2,
                'feels_like': 14.8,
                'humidity': 75,
                'wind_speed': 4.1,
                'icon': '10d'
            }
        }
        
        # Call the method
        result = self.weather_api.format_weather_response(weather_data)
        
        # Assertions
        self.assertIn('Weather in London, GB', result)
        self.assertIn('*Condition:* light rain', result)
        self.assertIn('*Temperature:* 15.2°C', result)
        self.assertIn('*Humidity:* 75%', result)
    
    def test_format_weather_response_error(self):
        # Test data
        weather_data = {
            'success': False,
            'error': 'Location not found'
        }
        
        # Call the method
        result = self.weather_api.format_weather_response(weather_data)
        
        # Assertions
        self.assertIn("Sorry, I couldn't get the weather information", result)
        self.assertIn("Location not found", result)

if __name__ == '__main__':
    unittest.main() 