import os
import pandas as pd
import sqlite3
import json

# Function to extract financial concepts from the dataframe
def extract_concepts(dataframe, concept_names):
    extracted_data = {}
    for concept_name in concept_names:
        concept_values = dataframe[dataframe['concept'] == concept_name]['value']
        extracted_data[concept_name] = concept_values.values.tolist()
    return extracted_data

# Example usage
folder_path = '/Users/camkish/Downloads/companyfacts'
concept_names = ['Revenues', 'NetIncomeLoss', 'Assets', 'Liabilities']  # Specify the concepts you want to extract
database_path = "sec2.db"  # Path to SQLite database file

# Initialize an empty dataframe
df = pd.DataFrame()


# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = file.read()
            json_data = json.loads(data)
            facts = json_data['facts']
            temp_df = pd.DataFrame(facts.values())
            df = df.append(temp_df, ignore_index=True)

# Connect to SQLite database
conn = sqlite3.connect(database_path)

# Convert the dataframe to a SQLite table
financial_df.to_sql('financial_data', conn, if_exists='replace')

# Extract data from SQLite table
query = f"SELECT * FROM financial_data WHERE concept IN ({','.join(['?']*len(concept_names))})"
cursor = conn.cursor()
cursor.execute(query, concept_names)
extracted_data = cursor.fetchall()
cursor.close()

# Perform analysis on the extracted data
if len(extracted_data) > 0:
    extracted_df = pd.DataFrame(extracted_data, columns=df.columns)
    extracted_data = extract_concepts(extracted_df, concept_names)

    # Perform analysis using the extracted data

    # Calculate the average revenues
    revenues = extracted_data['Revenues']
    average_revenues = sum(revenues) / len(revenues)

    # Calculate the net income margin
    net_income = extracted_data['NetIncomeLoss']
    revenues = extracted_data['Revenues']
    net_income_margin = (sum(net_income) / sum(revenues)) * 100

    # Print the results
    print(f"Average Revenues: ${average_revenues:.2f}")
    print(f"Net Income Margin: {net_income_margin:.2f}%")

else:
    print("Some financial concepts not found in the data.")

# Close the database connection
conn.close()
