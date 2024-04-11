import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key         =os.environ.get("AZURE_OPENAI_API_KEY"),  
    api_version     ="2024-02-01",
    azure_endpoint  =os.environ.get("AZURE_OPENAI_ENDPOINT"),
)

response = client.chat.completions.create(    
    model   =   "gpt-35-turbo-0301",
    messages=[
        {"role": "system",      "content": "You are a helpful assistant."},
        {"role": "user",        "content": "Maryland capital?"}
  ]
)

print(response.choices[0].message.content)