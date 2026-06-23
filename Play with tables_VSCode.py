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

#### 3. Check All Teams

# Read Team table from the database into a DataFrame
teams = pd.read_sql("""SELECT *
                        FROM Team;""", conn)

print("=== All Teams ===")
print(teams)
print()

#### 4. Read the Full Match Table

# Read Match table from the database into a DataFrame
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

# Conclusion:
# - 12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
# - 3 columns with null values

print("=== All Matches ===")
print(matches)
print()

#### 5. Matches Won by Mumbai Indians (Team ID = 7)

MI_wins = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner = 7;""", conn)

print("=== Matches Won by Mumbai Indians ===")
print(MI_wins)
print()

#### 6. Mumbai Indians Wins in Seasons 8 and 9

MI_S8_S9 = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner = 7 AND Season_Id IN (8, 9);""", conn)

print("=== Mumbai Indians Wins in Seasons 8 & 9 ===")
print(MI_S8_S9)
print()

#### 7. Teams Whose Name Starts with 'De'

new_teams = pd.read_sql("""SELECT *
                        FROM Team
                        WHERE Team_Name LIKE 'De%';""", conn)

print("=== Teams Starting with 'De' ===")
print(new_teams)
print()

#### 8. Minimum and Maximum Win Margin

min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin)
                        FROM Match;""", conn)

print("=== Min and Max Win Margin ===")
print(min_max_margin)
print()

# Close the connection when done
conn.close()
