import json
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Set your Groq API key in your environment
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_prompt(company):
    name = company["name"]
    website = company["website"]
    employees = company["employees"]
    insights = company.get("insights", [])
    insights_text = "\n- ".join(insights) if insights else "No specific insights found."
    prompt = f"""
You are a B2B sales representative specializing in hardware solutions. Write a professional, personalized outreach message for the following company. Reference their business details and insights, and suggest relevant hardware solutions that could benefit them. Keep the tone professional and tailored for B2B outreach.

Company Name: {name}
Website: {website}
Employee Count: {employees}
Key Insights:\n- {insights_text}

Message:
"""
    return prompt

def get_groq_response(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.7
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print(f"Groq API error: {response.status_code} {response.text}")
        return "[Error generating message]"


def run_message_generation(input_file="company_insights.json", output_file="personalized_outreach.json"):
    with open(input_file, "r") as f:
        companies = json.load(f)

    results = []
    for company in companies[:10]:
        prompt = generate_prompt(company)
        name = company["name"]
        print(f"Generating message for {name}...")
        message = get_groq_response(prompt)
        result = {
            "name": company["name"],
            "website": company["website"],
            "employees": company["employees"],
            "insights": company.get("insights", []),
            "message": message
        }
        results.append(result)
        print(f"\n---\n{name} Outreach Message:\n{message}\n---\n")
        time.sleep(1)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Personalized outreach messages saved to {output_file}")
