import sqlite3

connection = sqlite3.connect('data/database.db')
cursor = connection.cursor()

def get(query):
    def decorator_get(func):
        def wrapper_get(*args, **kwargs):

            if not kwargs.get('params', False):
                cursor.execute(query)
            else:
                cursor.execute(query, kwargs.get('params'))

            kwargs.update({
                'result': cursor.fetchall()
            })

            return func(**kwargs)

        return wrapper_get
    return decorator_get
