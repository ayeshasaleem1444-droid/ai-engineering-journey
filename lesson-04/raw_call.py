import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found - check that .env exists in this folder")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
body = {
    "contents": [
        {"parts": [{"text": "Explain what an API key is in one sentence."}]}
    ]
}

request = urllib.request.Request(
    url,
    data=json.dumps(body).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    },
    method="POST",
)

with urllib.request.urlopen(request) as response:
    raw = json.loads(response.read())

print(json.dumps(raw, indent=2))
print("--- just the answer text ---")
print(raw["candidates"][0]["content"]["parts"][0]["text"])
