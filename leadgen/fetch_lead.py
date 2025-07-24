import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

def get_user_input():
    size_range = input("Enter company size range (e.g., '50-200 employees'): ").strip()
    industry = input("Enter industry/keywords (e.g., 'software', 'manufacturing'): ").strip()
    location = input("Enter location (optional): ").strip()
    return size_range, industry, location

def parse_size_range(size_range):
    # Extract min and max from input like "50-200 employees"
    try:
        parts = size_range.split()[0]  # "50-200"
        min_size, max_size = map(int, parts.split('-'))
        return min_size, max_size
    except Exception:
        print("Invalid size range format. Please use 'min-max employees'.")
        exit(1)

def fetch_leads(APOLLO_API_KEY, min_size, max_size, industry, location):
    url = "https://api.apollo.io/v1/organizations/search"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "x-api-key": APOLLO_API_KEY
    }
    payload = {
        "q_organization_keywords": industry,
        "organization_locations": [location] if location else [],
        "organization_num_employees_min": min_size,
        "organization_num_employees_max": max_size,
        "page": 1,
        "per_page": 20
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print("Error fetching leads:", response.text)
        exit(1)
    return response.json()

def save_leads_to_json(data, filename="leads.json"):
    companies = data.get("organizations", [])
    leads = []
    for company in companies:
        lead = {
            "name": company.get("name"),
            "website": company.get("website_url"),
            "employees": company.get("estimated_num_employees")
        }
        leads.append(lead)
    with open(filename, "w") as f:
        json.dump(leads, f, indent=2)

def run_lead_fetching():
    size_range, industry, location = get_user_input()
    min_size, max_size = parse_size_range(size_range)
    data = fetch_leads(APOLLO_API_KEY, min_size, max_size, industry, location)
    save_leads_to_json(data)
