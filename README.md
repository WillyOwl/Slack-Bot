# SlackBot - Agentic Slack Assistant

A Slack bot with agentic capabilities that can answer questions and perform tasks using external APIs.

## Features

- **Slack Integration**: Responds to direct messages and mentions in channels
- **LLM-Powered Responses**: Uses OpenAI's GPT models to generate helpful responses
- **Weather Information**: Provides current weather conditions for any location using OpenWeatherMap API
- **Agentic Capabilities**: Analyzes user intent and uses appropriate tools to fulfill requests

## Tech Stack

- **Backend**: Python
- **LLM Integration**: LangChain + OpenAI
- **Slack SDK**: Slack Bolt for Python
- **External API**: OpenWeatherMap API (authenticated)

## Architecture

The bot follows a modular architecture:

1. **Slack Bot Layer**: Handles Slack events and messages
2. **LLM Layer**: Processes user input and generates responses
3. **Tool Layer**: Integrates with external APIs (Weather)

### Architecture Diagram

```mermaid
flowchart TD
    A["User"] -->|"Messages"| B["Slack API"]
    B -->|"Events"| C["AipoBot"]
    C -->|"Process Message"| D{"Intent Analysis"}
    D -->|"Weather Intent"| E["Weather API Tool"]
    D -->|"General Intent"| F["LLM Response"]
    E -->|"API Call"| G["OpenWeatherMap API"]
    G -->|"Weather Data"| E
    E -->|"Formatted Response"| H["Response to User"]
    F -->|"Generated Response"| H
    H -->|"Send Message"| B
    B -->|"Display Message"| A
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Slack App credentials
- OpenAI API key
- OpenWeatherMap API key

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Copy the example environment file:
   ```
   cp .env.example .env
   ```

2. Edit the `.env` file with your actual credentials:
   ```
   # Slack API credentials
   SLACK_BOT_TOKEN=xoxb-your-bot-token
   SLACK_APP_TOKEN=xapp-your-app-token
   
   # OpenAI API credentials
   OPENAI_API_KEY=your-openai-api-key
   
   # Weather API credentials (if applicable)
   WEATHER_API_KEY=your-openweathermap-api-key
   
   # Server configuration
   PORT=3000
   ```

   **IMPORTANT**: Never commit your `.env` file to version control. It's already added to `.gitignore`.

### Slack App Setup

1. Create a new Slack App at [api.slack.com/apps](https://api.slack.com/apps)
2. Under "OAuth & Permissions", add the following scopes:
   - `app_mentions:read`
   - `chat:write`
   - `im:history`
   - `im:read`
   - `im:write`
3. Enable Socket Mode under "Socket Mode"
4. Enable Events API under "Event Subscriptions" and subscribe to:
   - `app_mention`
   - `message.im`
5. Install the app to your workspace
6. Copy the Bot Token, App Token, and Signing Secret to your `.env` file

### Running the Bot

```
python main.py
```

### Running Tests

To run the test suite:

```
python run_tests.py
```

## Usage

- Direct message the bot in Slack
- Mention the bot in a channel: `@AipoBot What's the weather in New York?`
- Ask general questions: `What is the capital of France?`
- Get weather information: `What's the weather like in Tokyo?`

## Project Structure

```
aipo_agent_bot/
├── app/
│   └── slack_bot.py      # Slack bot implementation
├── config/
│   └── config.py         # Configuration and environment variables
├── tests/
│   └── test_weather_api.py  # Unit tests for weather API
├── utils/
│   ├── llm.py            # LLM integration
│   └── weather_api.py    # Weather API integration
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
├── run_tests.py          # Script to run tests
└── README.md             # Project documentation
```
