import mysql.connector

"CREATE DATABASE IF NOT EXISTS alx_book_store;"
"USE alx_book_store;"


def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "leroymysql-1",
            database = "alx_book_store",
            port = 3306,

        )
        if connection.is_connected():
            print("Database alx_book_store created successfully!")
            return connection
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")


