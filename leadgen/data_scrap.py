import json
import requests
from bs4 import BeautifulSoup
import time

def extract_insights_from_website(url):
    insights = []
    if not url:
        return insights
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return insights
        soup = BeautifulSoup(response.text, 'html.parser')
        # Try to extract meta description and first 2-3 visible text snippets
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            insights.append(meta_desc['content'])
        # Try to get first 2-3 <p> tags with enough text
        p_tags = soup.find_all('p')
        for p in p_tags:
            text = p.get_text(strip=True)
            if text and len(text) > 40:
                insights.append(text)
            if len(insights) >= 3:
                break
    except Exception as e:
        pass  # Could log error if needed
    return insights[:3]

def run_scraper(input_file="leads.json", output_file="company_insights.json"):
    with open(input_file, 'r') as f:
        leads = json.load(f)

    results = []
    for lead in leads:
        name = lead.get('name')
        website = lead.get('website')
        print(f"Scraping insights for {name} ({website})...")
        insights = extract_insights_from_website(website)
        results.append({
            'name': name,
            'website': website,
            'employees': lead.get('employees'),
            'insights': insights
        })
        time.sleep(1)

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Scraping complete. Results saved to {output_file}")
