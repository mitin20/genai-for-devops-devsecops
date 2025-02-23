# Chat Model
#pip install --upgrade langchain langchain-community langchain-openai
#pip install -U langchain-ollama

# from langchain_ollama import OllamaLLM

# # Connect to the locally hosted deepseek-r1 model
# llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0.9)

# # Query the model
# text = "What is a good name for a framework that makes large language models easier to work with?"
# print(llm.invoke(text))  # or use llm.predict(text)

# Have a conversation
# from langchain_ollama import OllamaLLM
# from langchain_core.messages import SystemMessage, HumanMessage

# # Initialize the local chat model
# chat = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0, max_tokens=1000)

# # Set up initial context
# context = [SystemMessage(content="You are a friendly chatbot that likes to have conversations.")]

# while True:
#     user_message = input("You: ")
#     if user_message.lower() == "quit":
#         break

#     context.append(HumanMessage(content=user_message))

#     # Generate a response
#     response_text = chat.invoke(context)  # Returns a raw string
#     context.append(HumanMessage(content=response_text))  # Append as a message

#     print("AI:", response_text)


# Long chain agents
#pip install -U langchain langchain-ollama langchain-community wikipedia-api

# from langchain.agents import load_tools, initialize_agent, AgentType
# from langchain_ollama import OllamaLLM

# # Load the local LLM
# llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0)

# # Load tools
# tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# # Initialize the agent
# agent = initialize_agent(
#     tools, 
#     llm, 
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
#     verbose=True, 
#     handle_parsing_errors=True
# )

# # Run the agent with a question
# agent.run("How old is Michael Jordan? How long has it been since he retired from basketball?")


# Arxiv Summarizer Using Langchain
#pip install -U langchain langchain-ollama langchain-community arxiv

from langchain.agents import initialize_agent, AgentType, load_tools
from langchain_ollama import OllamaLLM

# Load the local LLM
llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0)

# Load tools (ArXiv for paper search)
tools = load_tools(["arxiv"], llm=llm)

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

# Run the agent with a query
agent.run("What is the most recent arXiv paper on large language models in the year 2023? What is the key insight from it?")



# extra openai library
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