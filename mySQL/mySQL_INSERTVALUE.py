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
        # Insert value(s)
        db_query = "INSERT INTO customers (name, address) VALUES (%s,%s)"
        val=("John","Highway 21")
        with connection.cursor() as cursor:
            cursor.execute(db_query, val)
            connection.commit() #Commit transaction
            print("1 record inserted with ID:",cursor.lastrowid) 
            print(cursor.rowcount, "record inserted") 

            #db_query = "INSERT INTO customers (name, address) VALUES (%s,%s)"
            val=("Michelle","Blue Village 1")

            cursor.execute(db_query, val)
            connection.commit() #Commit transaction
            print("1 record inserted with ID:",cursor.lastrowid) 
            print(cursor.rowcount, "total records inserted")
except Error as e:
    print(e)
    