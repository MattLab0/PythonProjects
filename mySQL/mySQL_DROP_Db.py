from getpass import getpass
from mysql.connector import connect, Error

# Get user credentials
username = input("Enter username: ")
password = getpass("Enter password: ")

try:
    # Connect to MySQL server (no need for a database)
    with connect(
        host="localhost",
        user=username,
        password=password,
    ) as connection:
        with connection.cursor() as cursor:
            # Drop the database
            drop_db_query = "DROP DATABASE IF EXISTS online_movie_rating"
            cursor.execute(drop_db_query)
            print("Database deleted successfully.")

except Error as e:
    print(f"Error: {e}")
