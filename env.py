import os
import openai

def init_api():
    with open("README.md") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")

init_api()

print("\n1st: " + openai.api_key)
print("2nd: " + openai.organization + "\n")