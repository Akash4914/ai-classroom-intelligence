import sqlite3

conn = sqlite3.connect("data/attendance.db")

cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM attention").fetchall()

for row in rows:
    print(row)