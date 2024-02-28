import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key         =os.environ.get("AZURE_OPENAI_API_KEY"),  
    api_version     ="2023-12-01-preview",
    azure_endpoint  =os.environ.get("AZURE_OPENAI_ENDPOINT"),
)

response = client.chat.completions.create(    
    model   =   os.environ.get("AZURE_DEPLOYMENT"),
    messages=[
        {"role": "system",      "content": "You are a helpful assistant."},
        {"role": "user",        "content": "Maryland capital?"}
  ]
)

print(response.choices[0].message.content)