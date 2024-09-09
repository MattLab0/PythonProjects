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
        # Simulate unsafe SQL injection
        user_input = "'' OR '1'='1'"  # This is an unsafe injection string
        
        # # Unsafe query construction
        # db_query = f"SELECT name, address FROM customers WHERE name = {user_input}"
        
        # # Debug print the constructed query
        # print("Debug Query:", db_query)

        # Use parameterized queries to prevent SQL injection
        db_query = "SELECT name, address FROM customers WHERE name = %s"
        
        with connection.cursor() as cursor:
            #cursor.execute(db_query) #unsafe
            cursor.execute(db_query, (user_input,))
            result = cursor.fetchall()
            for x in result:
                print(x)
except Error as e:
    print(e)
