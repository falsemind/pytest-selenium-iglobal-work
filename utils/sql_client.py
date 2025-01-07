import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None

    try:
        print("Connecting to DB...")
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Successfully connected to DB.")

    except Error as err:
        print(f"Failed to connect to DB: '{err}'")

    return connection

def execute_sql_query(connection, query, params=None):
    result = None
    cursor = connection.cursor(dictionary=True)

    try:
        print("Executing query...")
        cursor.execute(query, params)
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()

            if len(result) == 0:
                result = None

        else:
            connection.commit()

    except Error as e:
        print(f"Error while executing query: '{e}'")

    finally:
        cursor.close()

    print("Successfully executed query.")
    return result
