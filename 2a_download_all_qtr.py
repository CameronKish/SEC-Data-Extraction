import requests
from bs4 import BeautifulSoup
import os

# URL of the SEC data sets page
url = "https://www.sec.gov/dera/data/financial-statement-data-sets"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Directory to save the downloaded ZIP files
save_dir = "/Users/camkish/Documents/Python/XBRL_Extraction/SECFilings"

# Iterate through the links
for link in links:
    href = link.get("href")
    if href and href.endswith(".zip"):  # Check if href is not None
        # Construct the URL of the ZIP file
        file_url = f"https://www.sec.gov{href}"

        # Extract the filename from the URL
        file_name = os.path.basename(file_url)

        # Create the file path to save the ZIP file
        file_path = os.path.join(save_dir, file_name)

        # Download the ZIP file
        response = requests.get(file_url)
        response.raise_for_status()

        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded: {file_name}")

print("All ZIP files downloaded.")
