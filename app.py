import sqlite3
con = sqlite3.connect("income.db")
cur = con.cursor()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS salary(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT UNIQUE,
    total_salary INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );'''
)

cur.execute(
    ''' INSERT INTO salary (id, month, total_salary) VALUES (4, "May", 5000)'''
)
con.commit()

cur.execute("SELECT * FROM salary")
rows = cur.fetchall()
for row in rows:
    print(row)

con.close()

# use sqlite viewer extension 

