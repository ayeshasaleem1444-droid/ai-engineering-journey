import "dotenv/config";
import { GoogleGenAI } from "@google/genai";

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  throw new Error("GEMINI_API_KEY not found - check that .env exists in this folder");
}

const ai = new GoogleGenAI({ apiKey });

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Explain what an API key is in one sentence.",
});

console.log(response.text);
