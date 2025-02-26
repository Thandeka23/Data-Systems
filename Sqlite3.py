import sqlite3

# Create a database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Insert data
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
print(cursor.fetchall())

# Close the connection
conn.close()