import json
import sqlite3

# Specify the JSON file path
json_file_path = 'CIK0000927003.json'

# Specify the SQLite database path
database_path = 'sec2.db'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = file.read()
    json_data = json.loads(data)

# Extract the column values
cik = json_data['cik']
entity_name = json_data['entityName']
facts = json_data['facts']

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Create a table in the database
table_name = 'financial_data'
create_table_query = '''
CREATE TABLE IF NOT EXISTS {table_name} (
    cik TEXT,
    entityName TEXT,
    facts TEXT
)
'''.format(table_name=table_name)
cursor.execute(create_table_query)

# Insert the data into the table
insert_query = 'INSERT INTO {table_name} (cik, entityName, facts) VALUES (?, ?, ?)'.format(table_name=table_name)
cursor.execute(insert_query, (cik, entity_name, json.dumps(facts)))

# Commit the changes and close the connection
conn.commit()
conn.close()
