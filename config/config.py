import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Slack API credentials
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# OpenAI API credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Weather API credentials (OpenWeatherMap)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Server configuration
PORT = int(os.getenv("PORT", 3000))