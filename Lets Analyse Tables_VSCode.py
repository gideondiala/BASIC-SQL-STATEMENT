#### 1. Connect with SQLite Database

# Import necessary libraries
import sqlite3
import pandas as pd
import os

# --- PATH SETUP ---
# Build the path to the database file relative to this script's location
# This works on both Windows and macOS without changing anything
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(BASE_DIR, 'database.sqlite')

# Connect to the SQLite database
conn = sqlite3.connect(database)
print('Opened database successfully')
print()

#### 2. List All Tables in the Database

# Read SQL query to get all tables from the database into a DataFrame
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)

print("=== All Tables in Database ===")
print(tables)
print()

#### 3. Read and Inspect the Match Table

# Read Match table from the database into a DataFrame
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

# Print table info (column names, types, null counts)
print("=== Match Table Info ===")
matches.info()
print()

# Close the connection when done
conn.close()
