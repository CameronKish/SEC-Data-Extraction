import json

# Specify the JSON file path
json_file_path = 'CIK0000927003.json'
import json

def print_json_layers(data, file, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            file.write('  ' * indent + str(key) + '\n')
            print_json_layers(value, file, indent + 1)
    elif isinstance(data, list):
        for item in data:
            print_json_layers(item, file, indent)
    else:
        file.write('  ' * indent + str(data) + '\n')

# Load the JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Open a new file to write the layers
with open('output.txt', 'w') as output_file:
    # Print the layers of the JSON data to the file
    print_json_layers(json_data, output_file)
