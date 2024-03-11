import requests
import sqlite3

# URL of the JSON file
url = "https://www.sec.gov/files/company_tickers.json"

# Fetch the JSON data from the URL
response = requests.get(url)
data = response.json()

# Connect to the SQLite database
conn = sqlite3.connect('2023q1.db')
cursor = conn.cursor()

# Create the ticker_table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS ticker_table (
                    cik TEXT,
                    ticker TEXT PRIMARY KEY,
                    name TEXT
                )''')

# Insert data into the ticker_table
for key, item in data.items():
    cik = str(item["cik_str"])
    ticker = item["ticker"]
    name = item["title"]

    # Execute the INSERT statement
    cursor.execute('INSERT INTO ticker_table VALUES (?, ?, ?)', (cik, ticker, name))

# Commit the changes and close the connection
conn.commit()
conn.close()
