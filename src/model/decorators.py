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
                'result': cursor
            })

            return func(**kwargs)

        return wrapper_query
    return decorator_query


def insert(query_string):

    def decorator_insert(func):
        def wrapper_insert(*args, **kwargs):

            if not kwargs.get('params', False):
                raise Exception('Not params found')

            params = kwargs.get('params')

            if isinstance(params, tuple):
                result = cursor.execute(query_string, params)
            elif isinstance(params, list):
                result = cursor.executemany(query_string, params)
            else:
                raise Exception('Invalid params type')

            connection.commit()

            kwargs.update({'result': result.rowcount})
            return func(**kwargs)

        return wrapper_insert
    return decorator_insert
