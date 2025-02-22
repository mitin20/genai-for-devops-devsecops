# ref https://docs.gpt4all.io/index.html
from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads model from https://huggingface.co/
with model.chat_session():
    print(model.generate("Write a Deployment YAML file to deploy container on EKS where container name is hello-application", max_tokens=1024))