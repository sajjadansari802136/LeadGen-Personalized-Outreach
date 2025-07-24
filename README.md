# Lead Generation & Personalized Outreach

## Overview
This project automates the process of lead generation, company insights scraping, and personalized outreach message generation. It consists of three main steps:

1. **Fetch leads from Apollo API**
2. **Scrape insights from company websites**
3. **Generate personalized outreach messages**

## Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Wednesday-Assignment
   ```
2. **Create virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
Run the main pipeline:
```bash
python main.py
```

### What happens?
- **Step 1:** Fetches leads from the Apollo API and saves them locally.
- **Step 2:** Scrapes company websites for insights and saves them to `company_insights.json`.
- **Step 3:** Generates personalized outreach messages for each lead using the scraped insights.

---

## Customization
- **API Keys & Config:**
  - If your scripts require API keys or environment variables, create a `.env` file in the root directory and add your secrets there.
- **Output Files:**
  - Leads and insights are saved as JSON files in the project root.

---

## Requirements
- Python 3.7+
- See `requirements.txt` for Python package dependencies.

---
