#don't run this. Attempted to move json into a table. not work
#import json
import sqlite3
from collections import deque

# Function to flatten nested JSON structure into a tabular format
def flatten_json(json_data, parent_key='', sep='_'):
    flattened_data = {}
    for key, value in json_data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, parent_key=new_key, sep=sep))
        elif isinstance(value, list):
            queue = deque(value)
            while queue:
                item = queue.popleft()
                if isinstance(item, dict):
                    for k, v in item.items():
                        new_key = f"{parent_key}{sep}{key}{sep}{k}" if parent_key else f"{key}{sep}{k}"
                        queue.append({new_key: v})
                else:
                    flattened_data[new_key] = item
        else:
            flattened_data[new_key] = value
    return flattened_data

# Read JSON data from file
json_file = 'CIK0000927003.json'
with open(json_file, 'r') as file:
    json_data = json.load(file)

# Flatten the nested JSON data
flattened_data = flatten_json(json_data)

# Extract the column names and row values from the flattened data
column_names = list(flattened_data.keys())
row_values = list(flattened_data.values())

# Create a SQLite connection
conn = sqlite3.connect("sec2.db")
cursor = conn.cursor()

# Create the table with inferred schema
create_table_query = f"CREATE TABLE IF NOT EXISTS AE_json ({', '.join(column_names)})"
cursor.execute(create_table_query)

# Insert the row values into the table
insert_row_query = f"INSERT INTO AE_json VALUES ({', '.join(['?']*len(column_names))})"
cursor.execute(insert_row_query, row_values)

# Commit the changes and close the connection
conn.commit()
conn.close()
print("done")
