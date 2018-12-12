import sqlite3

connection = sqlite3.connect('data/database.db')
cursor = connection.cursor()

def get(query):
    def decorator_get(func):
        def wrapper_get(*args, **kwargs):

            cursor.execute(query)
            return func(*args, cursor.fetchall(), **kwargs)

        return wrapper_get
    return decorator_get
