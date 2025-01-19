from openai import OpenAI
import google.generativeai as genai
from fastapi import FastAPI
import os

OPENAI_API_KEY="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"
GEMINI_API_KEY="AIzaSyD8K4xnMh9Hq-26x0aRaTPM88FTlh-qtqk"


client = OpenAI(api_key=OPENAI_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

# Initialize FastAPI app
app = FastAPI()

def fetch_openai_summary(company_name = "anthropic"):
    """ Fetch company summary from OpenAI's GPT. """
    prompt = f"Provide a structured due diligence summary for {company_name}. Include an overview, founders, funding history, and key risks."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True, messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message


def fetch_gemini_summary(company_name = "anthropic"):
    """ Fetch company summary from Google Gemini. """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize due diligence for {company_name}")
    return response.text

@app.get("/due_diligence/{company}")
def get_due_diligence(company: str):
    """ API Endpoint: Fetches company due diligence summary from AI models. """
    openai_summary = fetch_openai_summary(company)
    gemini_summary = fetch_gemini_summary(company)

    return {
        "company": company,
        "openai_summary": openai_summary,
        "gemini_summary": gemini_summary
    }

if __name__ == '__main__':
    print("test")
    XX = fetch_openai_summary()
    # XX = fetch_gemini_summary()
    print(XX)
    print("after test")