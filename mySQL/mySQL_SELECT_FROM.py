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
        db_query = "SELECT*FROM customers"
        with connection.cursor() as cursor:
            cursor.execute(db_query)
            result=cursor.fetchall()
            for x in result:
                print(x) 
except Error as e:
    print(e)