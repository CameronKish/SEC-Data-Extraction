import json

# Specify the JSON file path
json_file_path = 'CIK0000927003.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = file.read()
    json_data = json.loads(data)

# Check if the JSON data is a single dictionary
if isinstance(json_data, dict):
    # Extract the column names from the dictionary keys
    column_names = list(json_data.keys())
else:
    # JSON data has an unexpected structure
    column_names = []

# Print the column names
print(column_names)
