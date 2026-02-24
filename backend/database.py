import sqlite3


# Connect database
conn = sqlite3.connect("data/attendance.db")

cursor = conn.cursor()


# Create attendance table
cursor.execute("""

CREATE TABLE IF NOT EXISTS attention (

id INTEGER PRIMARY KEY AUTOINCREMENT,

student_id TEXT,

status TEXT,

duration REAL,

date TEXT,

time TEXT

)

""")

conn.commit()
print("Database Ready")