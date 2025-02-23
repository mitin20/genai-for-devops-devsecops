# goto https://colab.research.google.com/drive/xxx

# langchain and openai install
```
pip install --upgrade langchain langchain-community
```


# set openai token
```
import os
from langchain_community.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

llm = OpenAI(temperature=0.9)

text = "What is a good name for a framework that makes large language models easier to work with?"

print(llm.invoke(text))  # or use llm.predict(text)
```


# Connect to Hugging Face Hub
```
!pip install huggingface_hub > /dev/null
     
```

```
from getpass import getpass

HUGGINGFACEHUB_API_TOKEN = getpass()
```    

```
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
```

     
```
from langchain_community.llms import HuggingFaceHub

repo_id = "google/flan-t5-base" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0, "max_length":64})
llm
```     

```
text = "Please answer the following question. What is the boiling point of water in farenheit?"

llm(text)
     
```


# Chat Models
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
     

# Have A Conversation
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
