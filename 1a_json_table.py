import sqlite3
import os
import json

# Connect to the database
conn = sqlite3.connect('sec2.db')
cursor = conn.cursor()

# Define the folder path containing the JSON files
folder_path = '/Users/camkish/Downloads/submissions'

# Create a new table to store the compiled data
table_name = 'submissions_table'
cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                    cik TEXT,
                    name TEXT,
                    sic TEXT,
                    addresses TEXT,
                    filings TEXT
                )''')

# Set the loop counter
loop_count = 0

# Iterate over the JSON files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if loop_count >= 100:
        break

    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # Extract the relevant fields from the JSON data
    cik = json_data.get('cik')
    name = json_data.get('name')
    sic = json_data.get('sic')
    addresses = json.dumps(json_data.get('addresses'))
    filings = json.dumps(json_data.get('filings'))

    # Insert the data into the table
    cursor.execute(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)',
                   (cik, name, sic, addresses, filings))
    loop_count += 1
    print(loop_count)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully.")
