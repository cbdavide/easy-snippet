import sqlite3

connection = sqlite3.connect('data/database.db')
cursor = connection.cursor()


def query(query_string):

    def decorator_query(func):
        def wrapper_query(*args, **kwargs):

            if not kwargs.get('params', False):
                cursor.execute(query_string)
            else:
                cursor.execute(query_string, kwargs.get('params'))

            kwargs.update({
                'result': cursor.fetchall()
            })

            return func(**kwargs)

        return wrapper_query
    return decorator_query
