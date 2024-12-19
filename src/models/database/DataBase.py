import sqlite3

class DataBase:
    def __init__(self):
        self.database_path = "C:\\Users\\Compras\\Documents\\Repositorios\\integracao-resulth-clickup\\src\\models\\database\\database.db"

    def __check_sql(self, sql):
        return sql.strip().upper().startswith(("INSERT", "DELETE", "UPDATE", "CREATE"))

    def query(self, query_object):
        connection = None
        try:
            connection = sqlite3.connect(self.database_path)
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            sql = query_object.get("sql")
            params = query_object.get("params")

            print(f"Executing SQL: {sql}")
            if params:
                print(f"With params: {params}")
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            # Commit for modifying queries
            if self.__check_sql(sql):
                connection.commit()
                print("Changes committed successfully.")
                return

            # Fetch and return results for SELECT queries
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

        except sqlite3.Error as e:
            print("Database Error:", e)
            raise

        finally:
            if connection:
                print("Connection closed.")
                connection.close()
