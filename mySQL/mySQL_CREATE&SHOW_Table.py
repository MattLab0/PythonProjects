from getpass import getpass
from mysql.connector import connect, Error

# Get user credentials
username = input("Enter username: ")
password = getpass("Enter password: ")

try:
    with connect(
        host="localhost",
        user=username,
        password=password,
        database="online_movie_rating",
    ) as connection:
        # Create table
        table_db_query = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
        with connection.cursor() as cursor:
            cursor.execute(table_db_query)
    with connect(
        host="localhost",
        user=username,
        password=password,
        database="online_movie_rating",
    ) as connection:
        # Show table(s)
        show_table_db_query = "SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(show_table_db_query)
            for x in cursor:
                print(x)
except Error as e:
    print(e)