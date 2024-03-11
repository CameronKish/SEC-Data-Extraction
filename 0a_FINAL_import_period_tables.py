#This imports the .txt files from the quarter into tables in the sec.db

import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('2023q1.db')
cursor = conn.cursor()

# Define the folder path
folder_path = '/Users/camkish/Documents/Python/XBRL_Extraction/2023q1'

# Define column definitions for each file
column_defs = {
    'num.txt': [
        'adsh TEXT',
        'tag TEXT',
        'version TEXT',
        'coreg TEXT',
        'ddate TEXT',
        'qtrs TEXT',
        'uom TEXT',
        'value TEXT',
        'footnote TEXT'
    ],
    'pre.txt': [
        'adsh TEXT',
        'report TEXT',
        'line TEXT',
        'stmt TEXT',
        'inpth TEXT',
        'rfile TEXT',
        'tag TEXT',
        'version TEXT',
        'plabel TEXT',
        'negating TEXT'
    ],
    'sub.txt': [
        'adsh TEXT',
        'cik TEXT',
        'name TEXT',
        'sic TEXT',
        'countryba TEXT',
        'stprba TEXT',
        'cityba TEXT',
        'zipba TEXT',
        'bas1 TEXT',
        'bas2 TEXT',
        'baph TEXT',
        'countryma TEXT',
        'stprma TEXT',
        'cityma TEXT',
        'zipma TEXT',
        'mas1 TEXT',
        'mas2 TEXT',
        'countryinc TEXT',
        'stprinc TEXT',
        'ein TEXT',
        'former TEXT',
        'changed TEXT',
        'afs TEXT',
        'wksi TEXT',
        'fye TEXT',
        'form TEXT',
        'period TEXT',
        'fy TEXT',
        'fp TEXT',
        'filed TEXT',
        'accepted TEXT',
        'prevrpt TEXT',
        'detail TEXT',
        'instance TEXT',
        'nciks TEXT',
        'aciks TEXT'
    ],
    'tag.txt': [
        'tag TEXT',
        'version TEXT',
        'custom TEXT',
        'abstract TEXT',
        'datatype TEXT',
        'iord TEXT',
        'crdr TEXT',
        'tlabel TEXT',
        'doc TEXT'
    ]
}

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    table_name = os.path.splitext(file_name)[0] + '_table'

    # Get the column definitions for the current file
    if file_name in column_defs:
        columns = column_defs[file_name]
    else:
        print(f"Column definitions not found for file: {file_name}")
        continue

    # Create the table if it doesn't exist
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        {", ".join(columns)}
                    )''')

    # Read the data from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Insert the data into the table
    for line in lines[1:]:
        data = line.strip().split('\t')
        num_columns = len(data)

        # Append None for missing values
        if num_columns < len(columns):
            data.extend([None] * (len(columns) - num_columns))

        # Generate the placeholders for the SQL statement
        placeholders = ','.join(['?'] * len(columns))
        insert_sql = f'INSERT INTO {table_name} VALUES ({placeholders})'

        cursor.execute(insert_sql, data)

# Commit the changes and close
conn.commit()
conn.close()