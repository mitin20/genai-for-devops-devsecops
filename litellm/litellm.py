# using ollama mac server
# pip install litellm
# from litellm import completion

# response = completion(
#     model="ollama/llama2", 
#     messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
#     api_base="http://localhost:11434"
# )
# print(response)


# using ;ittellm/ollama
import openai

api_base = f"http://0.0.0.0:11434" # base url for server

openai.api_base = api_base
openai.api_key = "ollama"
print(openai.api_base)


print(f'LiteLLM: response from proxy with streaming')
response = openai.chat.completions.create(
    model="ollama/llama3.2", 
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