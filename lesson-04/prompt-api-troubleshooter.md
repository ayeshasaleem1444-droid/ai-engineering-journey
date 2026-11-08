# API Troubleshooter — Lesson 04 (Gemini route, Ayesha)

Use this checklist when an LLM API call fails. Work top to bottom.

## Golden rules
- The API key lives ONLY in .env. Never in code, never in a commit, never pasted into chat.
- Verify a key without showing it: print the variable NAME and the value's LENGTH, never the value. (My Gemini key: prefix AQ., length 53 — the newer Google format. Older keys start AIza and are 39 long.)
- Read errors from the BOTTOM line of the traceback. Everything above is just the path.
- Find the HTTP status code first. 4xx = my request is wrong. 5xx = the server's side. The fix is different for each.

## Errors I have actually met
- 400 API_KEY_INVALID "API key not valid" — the key is wrong, missing, or not loaded. Check: does .env exist in this folder? Is the variable name exactly GEMINI_API_KEY? Did load_dotenv() run before creating the client?
- 404 NOT_FOUND model "no longer available to new users" — the model name is retired. Do not guess names: run a list-models call and pick an exact name from the list my key can see. (For me, gemini-3.5-flash works.)
- 503 UNAVAILABLE "high demand" — the server is overloaded, my request is fine. Change nothing. Wait a few minutes and retry once. If the newest model is hot, an older Flash model may answer sooner.
- 429 rate limit — too many requests too fast (free tier is roughly 10-15 per minute). Slow down, wait, retry with patience.
- The call hangs with no prompt back — a stalled connection or a server in retry loops. Ctrl+C is safe (the program only asks a question). Wait, then retry once.

## Diagnostic order
1. Am I in the right environment? (venv active for Python — prompt prefix; fnm Node v22 for TypeScript — which node shows fnm_multishells.)
2. Is .env present and is the variable name exact? (Check name + length, never the value.)
3. Does the key authenticate? Clue: if the error is about the MODEL, the key already passed.
4. Does the model exist for my key? (List models; pick an exact name.)
5. Read the status class: 4xx fix the request, 5xx wait and retry.

## When asking for help
Paste only: the status code and the error message body. Never the key.
