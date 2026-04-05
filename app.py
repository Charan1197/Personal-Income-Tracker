import sqlite3
con = sqlite3.connect("income.db")
cur = con.cursor()

cur.execute(
    '''CREATE TABLE salary(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT UNIQUE,
    total_salary INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );'''
)

