import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found — check the .env file in this folder")

client = genai.Client(api_key=api_key)

for model in client.models.list():
    print(model.name)
