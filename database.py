import sqlite3
from datetime import datetime

#functions
def add_coordinates(x, y, time):
    # Connect to the database
    conn = sqlite3.connect('coordinates.db')
    cursor = conn.cursor()

    # Insert info into the table
    cursor.execute("""
    INSERT INTO coordinates (x, y, timestamp) VALUES (?, ?, ?);
    """, (x, y, time))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def print_coordinates():
    # Connect to the database
    conn = sqlite3.connect('coordinates.db')
    cursor = conn.cursor()

    # Query all rows from the table
    cursor.execute("SELECT * FROM coordinates ORDER BY timestamp DESC;")
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

#check if db exists then connect if it does and create if not
conn = sqlite3.connect('coordinates.db')
cursor = conn.cursor()

#Create a table to store the coordinates and timestamp
cursor.execute("""
CREATE TABLE IF NOT EXISTS coordinates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    timestamp DATETIME NOT NULL
);
""")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Coordinates table created")


# Example usage
x = 10
y = 20
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

add_coordinates(x, y, time)
print_coordinates()