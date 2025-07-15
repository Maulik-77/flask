import sqlite3

conn = sqlite3.connect("admin.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(results)")
columns = cursor.fetchall()

for col in columns:
    print(f"{col[0]} | {col[1]} | {col[2]} | Not Null: {col[3]} | Default: {col[4]} | PK: {col[5]}")
