import sqlite3

conn = sqlite3.connect('data/database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE repository
                        (user text, name text)''')

cursor.execute('''INSERT INTO repository VALUES ('cbdavide', 'easy-snippet')''')

conn.commit()
