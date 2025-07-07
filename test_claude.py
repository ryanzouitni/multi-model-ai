import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Claude API endpoint
url = "https://api.anthropic.com/v1/messages"

# HTTP headers required by Anthropic
headers = {
    "x-api-key": CLAUDE_API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

# Use a model you have access to (from limits page)
payload = {
    "model": "claude-3-haiku-20240307",  # ✅ You are allowed to use this model
    "max_tokens": 300,
    "messages": [
        {"role": "user", "content": "Tell me a fun fact about space."}
    ]
}

# Send request
response = requests.post(url, headers=headers, json=payload)

# Print raw response for debugging
print("Claude Response:")
print("Status Code:", response.status_code)
print(response.text)
