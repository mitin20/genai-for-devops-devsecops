# goto https://colab.research.google.com/drive/xxx

# langchain and openai install
pip install langchain
pip install openai

# set openai token
import os
os.environ["OPENAI_API_KEY"] = "YOUR API KEY"

from langchain.1lms import OpenAI


llm = OpenAI(temperature-0.9)


text = "What is a good name for a framework that makes large language models easier to work with?"

print(llm(text))
