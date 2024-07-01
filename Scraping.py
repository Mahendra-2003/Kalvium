import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
tables = soup.find_all('table')
if not tables:
    print("No tables found on the page.")
else:
    def parse_party_results(table):
        party_results = []
        for row in table.find_all('tr')[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) >= 4:  # Ensure there are enough columns
                party_results.append({
                    'Party': cols[0].text.strip(),
                    'Won': cols[1].text.strip(),
                    'Leading': cols[2].text.strip(),
                    'Total': cols[3].text.strip()
                })
        return party_results

    party_results = parse_party_results(tables[0])
    df_party_results = pd.DataFrame(party_results)
    df_party_results.to_csv('Lok_Sabha_Election_Results_2024-1.csv', index=False)
    print("Current Working Directory:", os.getcwd())
    print("Data successfully scraped and saved")

