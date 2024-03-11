#Joins tables to get only 10k submission data for the quarter (which is the 10k here)

import sqlite3

# Connect to the database
conn = sqlite3.connect('sec.db')
cursor = conn.cursor()

# Perform the join and select query
query = '''
    CREATE TABLE IF NOT EXISTS AE_10k AS
    SELECT *
    FROM sub_table
    INNER JOIN num_table ON sub_table.adsh = num_table.adsh
    WHERE sub_table.cik = '927003' AND sub_table.form = '10-K'
'''

# Execute the query
cursor.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
