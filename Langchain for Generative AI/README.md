# Prerequisites for local runs

## Create a new conda environment with Python 3.12
```
conda create -n genai python=3.12
```
## Activate the environment
```
conda activate genai
```

## Install required packages
```
conda install -c conda-forge langchain-community
conda install -c huggingface huggingface-hub
conda install -c conda-forge sentence-transformers
```

## Verify Python version
```
python --version
```

## List all conda environments
```
conda env list
```

## To deactivate the environment when you're done
```
conda deactivate
```


# Prerequisites for local runs
```
open https://colab.research.google.com/drive/xxx
```

# langchain and openai install
```
pip install --upgrade langchain langchain-community
```


## set openai token
```
import os
from langchain_community.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

llm = OpenAI(temperature=0.9)

text = "What is a good name for a framework that makes large language models easier to work with?"

print(llm.invoke(text))  # or use llm.predict(text)
```


## Connect to Hugging Face Hub
```
pip install huggingface_hub > /dev/null
     
```
curl -X GET "https://huggingface.co/api/whoami" -H "Authorization: Bearer YOUR_HUGGINGFACE_API_TOKEN"
```
pip install langchain-community huggingface_hub
```     

```
import os
from langchain_community.llms import HuggingFaceHub

# Set API token (replace with your actual token)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_huggingface_api_token"

repo_id = "google/flan-t5-base"

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0, "max_length": 64})

text = "Please answer the following question. What is the boiling point of water in Fahrenheit?"

print(llm.invoke(text))  # Use .invoke() instead of calling the object directly     
```


## Chat Models
```
from langchain_openai import ChatOpenAI
from langchain.schema import (
    AIMessage, # AI input
    HumanMessage, # user input
    SystemMessage # sets the tone of the conversation
)

chat = ChatOpenAI(temperature=0,
                  max_tokens=100)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
chat.invoke(messages)
```
     

## Have A Conversation
```
chat = ChatOpenAI(temperature=0,
                  max_tokens=1000)

context = [SystemMessage(content="You are a friendly Chatbot that likes to have conversations.")]

while True:
    user_message = input("You: ")
    context.append(HumanMessage(content=user_message))
    if user_message.lower() == "quit":
        break
    response = chat.invoke(context)

    context.append(response)
    print("AI: ", response.content)
```   

# No OpenAI Key?
```
ollama run deepseek-r1:1.5b
```
```
pip install --upgrade langchain langchain-community langchain-openai
pip install -U langchain-ollama
```
```
# Chat Model
from langchain_ollama import OllamaLLM

# Connect to the locally hosted deepseek-r1 model
llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0.9)

# Query the model
text = "What is a good name for a framework that makes large language models easier to work with?"
print(llm.invoke(text))  # or use llm.predict(text)
```

```
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
```