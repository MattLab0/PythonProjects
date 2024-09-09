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
        database="food_preference"
    ) as connection:
        # Inner join
        select_query = """
        SELECT users.name as user, products.name as favorite 
        FROM users INNER JOIN products on users.favorite=products.id
        """
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            result=cursor.fetchall()
            print("Inner join table:")
            for x in result:
                print(x)
                
        # Left join 
        select_query = """
        SELECT users.name as user, products.name as favorite 
        FROM users LEFT JOIN products on users.favorite=products.id
        """
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            result=cursor.fetchall()
            print("Left join table:")
            for x in result:
                print(x)
                
        # Right join 
        select_query = """
        SELECT users.name as user, products.name as favorite 
        FROM users RIGHT JOIN products on users.favorite=products.id
        """
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            result=cursor.fetchall()
            print("Right join table:")
            for x in result:
                print(x)                 
except Error as e:
    print(f"Error: {e}")
