# langchain and openai install

#pip install --upgrade langchain langchain-community
# set openai token

# import os
# from langchain_community.llms import OpenAI

# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

# llm = OpenAI(temperature=0.9)

# text = "What is a good name for a framework that makes large language models easier to work with?"

# print(llm.invoke(text))  # or use llm.predict(text)


# Connect to Hugging Face Hub     
# Test HUGGINGFACE_API_TOKEN
#curl -X GET "https://huggingface.co/api/whoami" -H "Authorization: Bearer YOUR_HUGGINGFACE_API_TOKEN"

# Make sure you have the correct package installed:
#pip install langchain-community huggingface_hub langchain-huggingface python-dotenv
     
# import os
# import time
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient
# from huggingface_hub.utils import HfHubHTTPError

# # Load environment variables from .env file
# load_dotenv()

# # Get API token from environment
# api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
# if not api_token:
#     raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables")

# # Using a smaller, more reliable model
# model_id = "gpt2"  # Changed from flan-t5-base to gpt2

# def create_client(max_retries=3, retry_delay=2):
#     """Create InferenceClient with retry logic"""
#     for attempt in range(max_retries):
#         try:
#             client = InferenceClient(
#                 model=model_id,
#                 token=api_token
#             )
#             # Test the connection
#             client.text_generation("test")
#             return client
#         except HfHubHTTPError as e:
#             if "503" in str(e) and attempt < max_retries - 1:
#                 print(f"Service unavailable, retrying in {retry_delay} seconds...")
#                 time.sleep(retry_delay)
#                 continue
#             raise

# try:
#     # Create InferenceClient instance with retry logic
#     client = create_client()
    
#     text = "Please answer the following question. What is the boiling point of water in Fahrenheit?"
    
#     # Generate response using the appropriate task method
#     response = client.text_generation(
#         text,
#         max_new_tokens=64,
#         temperature=0.7,
#         top_p=0.95,
#         repetition_penalty=1.2
#     )
#     print("Response:", response)

# except HfHubHTTPError as e:
#     print(f"Error accessing Hugging Face API: {e}")
#     print("Suggestions:")
#     print("1. Check your internet connection")
#     print("2. Verify your API token is valid")
#     print("3. Try a different model")
#     print("4. The service might be temporarily down, try again later")
# except Exception as e:
#     print(f"Unexpected error: {e}")


# Have a conversation

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()

# Get API token from environment
api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
if not api_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables")

# Initialize the inference client
client = InferenceClient(
    model="gpt2",  # Using a conversational model
    token=api_token
)

# Initialize chat context
context = [
    SystemMessage(content="You are a friendly Chatbot that likes to have conversations.")
]

def get_chat_response(messages):
    """Get response using the appropriate task method"""
    # Combine all messages into a single context
    full_context = " ".join([msg.content for msg in messages])
    
    try:
        # Use text-generation task
        response = client.text_generation(
            full_context,
            max_new_tokens=100,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.2
        )
        return response

    except Exception as e:
        print(f"Error generating response: {e}")
        return "I apologize, but I'm having trouble generating a response right now."

def chat_loop():
    print("Chat started! Type 'quit' to exit.")
    print("AI: Hello! I'm your friendly chatbot. How can I help you today?")
    
    while True:
        try:
            # Get user input
            user_message = input("\nYou: ")
            
            # Check for quit command
            if user_message.lower() == "quit":
                print("\nAI: Goodbye! Have a great day!")
                break
            
            # Add user message to context
            context.append(HumanMessage(content=user_message))
            
            # Get AI response
            response = get_chat_response(context)
            
            # Add AI response to context
            ai_message = AIMessage(content=response)
            context.append(ai_message)
            
            # Print AI response
            print(f"\nAI: {response}")
            
        except Exception as e:
            print(f"\nError: {e}")
            print("Let's continue our conversation...")

if __name__ == "__main__":
    try:
        chat_loop()
    except KeyboardInterrupt:
        print("\nChat ended by user. Goodbye!")