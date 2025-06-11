import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", [
    ("Fabricio", 48),
    ("Alfredo", 36),
    ("Eunseok", 47),
    ("Yan", 30)
])
conn.commit()
conn.close()
