import requests
import json
from datetime import datetime

FACT_URL = "https://uselessfacts.jsph.pl/today.json?language=en"
output_path = "fact.json"

try:
    response = requests.get(FACT_URL)
    response.raise_for_status()
    fact_data = response.json()
    fact_text = fact_data.get("text", "No fact found today.")
except Exception as e:
    fact_text = f"Error fetching fact: {e}"

fact_json = {
    "fact": fact_text,
    "date": datetime.now().strftime("%B %d, %Y")
}

with open(output_path, "w") as f:
    json.dump(fact_json, f)