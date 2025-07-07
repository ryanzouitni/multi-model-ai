import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import requests
import google.generativeai as genai

load_dotenv()

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure APIs
openai.api_key = OPENAI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    model = data.get("model")
    prompt = data.get("prompt")


    if model == "ChatGPT":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response.choices[0].message["content"]

    elif model == "Claude":
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": "claude-3-haiku-20240307",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(url, headers=headers, json=data)
        output = response.json()["content"][0]["text"]

    elif model == "Gemini":
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        output = response.text if hasattr(response, "text") else str(response)


    else:
        output = "Invalid model selected."

    return jsonify({"response": output})


if __name__ == "__main__":
    app.run(debug=True)


