import json
import urllib.error
import urllib.request

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
body = {"contents": [{"parts": [{"text": "Say hello."}]}]}

request = urllib.request.Request(
    url,
    data=json.dumps(body).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "x-goog-api-key": "THIS-IS-A-FAKE-KEY",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print("HTTP status:", e.code)
    print(e.read().decode("utf-8"))
