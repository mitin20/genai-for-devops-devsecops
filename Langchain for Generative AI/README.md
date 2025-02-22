# goto https://colab.research.google.com/drive/xxx

# langchain and openai install

pip install --upgrade langchain langchain-community


# set openai token

import os
from langchain_community.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

llm = OpenAI(temperature=0.9)

text = "What is a good name for a framework that makes large language models easier to work with?"

print(llm.invoke(text))  # or use llm.predict(text)