#This imports just a single .txt into sec.db

import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('sec.db')
cursor = conn.cursor()

#define file path
folder_path = '/Users/camkish/Documents/Python/XBRL_Extraction/2023q1'
file_name = 'sub.txt'
file_path = os.path.join(folder_path, file_name)

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS sub_table (
                    adsh TEXT,
                    cik TEXT,
                    name TEXT,
                    sic TEXT,
                    countryba TEXT,
                    stprba TEXT,
                    cityba TEXT,
                    zipba TEXT,
                    bas1 TEXT,
                    bas2 TEXT,
                    baph TEXT,
                    countryma TEXT,
                    stprma TEXT,
                    cityma TEXT,
                    zipma TEXT,
                    mas1 TEXT,
                    mas2 TEXT,
                    countryinc TEXT,
                    stprinc TEXT,
                    ein TEXT,
                    former TEXT,
                    changed TEXT,
                    afs TEXT,
                    wksi TEXT,
                    fye TEXT,
                    form TEXT,
                    period TEXT,
                    fy TEXT,
                    fp TEXT,
                    filed TEXT,
                    accepted TEXT,
                    prevrpt TEXT,
                    detail TEXT,
                    instance TEXT,
                    nciks TEXT,
                    aciks TEXT
                )''')

# Read the data from the text file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Insert the data into the table
for line in lines[1:]:
    data = line.strip().split('\t')
    
    # Append None for missing values because length wasnt right without this apparently
    if len(data) < 36:
        data.extend([None] * (36 - len(data)))
    
    cursor.execute('''INSERT INTO sub_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully.")