import sqlite3

# Connect to the database
conn = sqlite3.connect('sec.db')
cursor = conn.cursor()

#this will select all the forms that were submitted for our selected company
cursor.execute("SELECT name, form FROM sub_table WHERE cik = '927003'")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)
    print("Done")

# Commit the changes and close the connection
conn.commit()
conn.close()