import sqlite3

class DataBase:
    def __init__(self):
        pass

    def query(self, query_object):
        try:
            connection = sqlite3.connect("database.db")
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            if query_object.get("params") is not None:
                cursor.execute(query_object.get("sql"), query_object.get("params"))
            else:
                cursor.execute(query_object["sql"])

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            return results
        except sqlite3.Error as e:
            print("Database Error", e)

        finally:
            if connection:
                connection.close()

