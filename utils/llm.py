from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from config.config import OPENAI_API_KEY

class LLMHandler:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o",
            api_key=OPENAI_API_KEY,
            temperature=0.7
        )
        
        self.system_prompt = """
        You are AipoBot, a helpful AI assistant integrated with Slack. 
        You can help users with various tasks including answering questions and checking the weather.
        Be concise, helpful, and friendly in your responses.
        """
        
    def generate_response(self, user_input, context=None):
        """Generate a response to user input using the LLM"""
        messages = [
            SystemMessage(content=self.system_prompt)
        ]
        
        if context:
            messages.append(SystemMessage(content=f"Context: {context}"))
            
        messages.append(HumanMessage(content=user_input))
        
        response = self.llm.invoke(messages)
        return response.content
        
    def analyze_intent(self, user_input):
        """Analyze user intent to determine if a specific tool should be used"""
        system_prompt = """
        Analyze the user's message and determine if they are requesting weather information.
        If they are asking about weather, return "weather" followed by the location.
        Otherwise, return "general".
        
        Examples:
        User: "What's the weather like in New York?"
        Response: "weather:New York"
        
        User: "Tell me about the weather in Paris"
        Response: "weather:Paris"
        
        User: "How are you today?"
        Response: "general"
        """
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]
        
        response = self.llm.invoke(messages)
        return response.content.strip() 