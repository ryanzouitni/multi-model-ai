import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model (use updated name!)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Generate content
response = model.generate_content("What is the capital of Morocco?")

# Print output
print("Gemini Response:")
print(response.text)

