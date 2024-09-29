import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://vit.ac.in/campuslife/hostels'

# Send request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table containing the Men's Hostel information
    table = soup.find_all('table')[1]  # Assuming the relevant table is the second one
    
    # Extract rows from the table
    rows = table.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:  # Ensure the row has two cells
            title = cells[0].get_text(strip=True)
            info = cells[1].get_text(strip=True, separator=' ')
            print(f"{title}: {info}")
else:
    print("Failed to retrieve the webpage.")
