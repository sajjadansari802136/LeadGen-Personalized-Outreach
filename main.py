from leadgen.fetch_lead import run_lead_fetching
from leadgen.data_scrap import run_scraper
from leadgen.AI_response import run_message_generation

def main():
    print("Step 1: Provide input and fetch leads from Apollo API...")
    run_lead_fetching()
    print("leads saved.")

    print("\nStep 2: Scraping insights from company websites...")
    run_scraper()
    print("Done")

    print("\nStep 3: Generating personalized outreach messages...")
    run_message_generation()
    print("Done")

if __name__ == "__main__":
    main()
