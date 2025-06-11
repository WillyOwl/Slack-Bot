import logging
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from utils.llm import LLMHandler
from utils.weather_api import WeatherAPI
from config.config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN, SLACK_SIGNING_SECRET

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Slack app
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

# Initialize handlers
llm_handler = LLMHandler()
weather_api = WeatherAPI()

@app.event("app_mention")
def handle_app_mention(event, say):
    """Handle mentions of the bot in channels"""
    user_id = event["user"]
    text = event["text"]
    
    # Remove the bot mention from the text
    cleaned_text = re.sub(r'<@[A-Z0-9]+>', '', text).strip()
    
    # Process the message
    process_message(cleaned_text, say, user_id)

@app.event("message")
def handle_direct_message(event, say):
    """Handle direct messages to the bot"""
    # Skip messages from the bot itself or messages in channels
    if "user" not in event or "channel_type" not in event or event["channel_type"] != "im":
        return
    
    user_id = event["user"]
    text = event["text"]
    
    # Process the message
    process_message(text, say, user_id)

def process_message(text, say, user_id):
    """Process incoming messages and generate appropriate responses"""
    # Analyze user intent
    intent = llm_handler.analyze_intent(text)
    
    # Check if weather intent is detected
    if intent.startswith("weather:"):
        location = intent.split(":", 1)[1].strip()
        weather_data = weather_api.get_weather(location)
        response = weather_api.format_weather_response(weather_data)
        say(response)
    else:
        # Handle general queries with LLM
        response = llm_handler.generate_response(text)
        say(response)

def start_bot():
    """Start the Slack bot"""
    try:
        logger.info("Starting AipoBot...")
        handler = SocketModeHandler(app, SLACK_APP_TOKEN)
        handler.start()
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise 