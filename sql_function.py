import sqlite3
from sqlite3 import Error



def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path, timeout=20)
        print("Connection to SQLite is successful")
    except Error as e:
        print(f"The error '{e}' occured")
    
    return connection

if __name__ == "__main__":
    pass