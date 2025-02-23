# Chat Model
# from langchain_ollama import OllamaLLM

# # Connect to the locally hosted deepseek-r1 model
# llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0.9)

# # Query the model
# text = "What is a good name for a framework that makes large language models easier to work with?"
# print(llm.invoke(text))  # or use llm.predict(text)

# Have a conversation
from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize the local chat model
chat = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0, max_tokens=1000)

# Set up initial context
context = [SystemMessage(content="You are a friendly chatbot that likes to have conversations.")]

while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        break

    context.append(HumanMessage(content=user_message))

    # Generate a response
    response_text = chat.invoke(context)  # Returns a raw string
    context.append(HumanMessage(content=response_text))  # Append as a message

    print("AI:", response_text)


# openai library
# from openai import OpenAI

# client = OpenAI(
#     base_url = 'http://localhost:11434/v1',
#     api_key='ollama', # required, but unused
# )

# response = client.chat.completions.create(
#   model="llama3.1",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The LA Dodgers won in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )
# print(response.choices[0].message.content)