import requests
from config.config import WEATHER_API_KEY

class WeatherAPI:
    def __init__(self):
        self.api_key = WEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        
    def get_weather(self, location):
        """Get current weather for a location"""
        try:
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'  # Use metric units (Celsius)
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            data = response.json()
            
            # Extract relevant weather information
            weather_info = {
                'location': data['name'],
                'country': data['sys']['country'],
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
            
            return {
                'success': True,
                'data': weather_info
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f"Error fetching weather data: {str(e)}"
            }
        except (KeyError, IndexError) as e:
            return {
                'success': False,
                'error': f"Error parsing weather data: {str(e)}"
            }
            
    def format_weather_response(self, weather_data):
        """Format weather data into a readable message"""
        if not weather_data['success']:
            return f"Sorry, I couldn't get the weather information: {weather_data['error']}"
            
        data = weather_data['data']
        
        message = (
            f"*Weather in {data['location']}, {data['country']}*\n"
            f"• *Condition:* {data['description']}\n"
            f"• *Temperature:* {data['temperature']}°C (feels like {data['feels_like']}°C)\n"
            f"• *Humidity:* {data['humidity']}%\n"
            f"• *Wind Speed:* {data['wind_speed']} m/s"
        )
        
        return message 