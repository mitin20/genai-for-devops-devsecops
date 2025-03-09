# An OpenAI API compatible server for local LLMs - llama2, mistral, codellama

## Quick Start:

Docker Hub: For ARM Processors: https://hub.docker.com/repository/docker/litellm/ollama/general For Intel/AMD Processors: to be added

docker pull litellm/ollama

docker run --name ollama litellm/ollama

## Test the server container

On the docker container run the test.py file using python3 test.py

Making a request to this server

import openai

api_base = f"http://0.0.0.0:4000" # base url for server

openai.api_base = api_base
openai.api_key = "temp-key"
print(openai.api_base)


print(f'LiteLLM: response from proxy with streaming')
response = openai.chat.completions.create(
    model="ollama/llama2", 
    messages = [
        {
            "role": "user",
            "content": "this is a test request, acknowledge that you got it"
        }
    ],
    stream=True
)

for chunk in response:
    print(f'LiteLLM: streaming response from proxy {chunk}')