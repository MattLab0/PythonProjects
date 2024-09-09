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
        update_query = "UPDATE customers SET address = %s WHERE address = %s" 
        val = ("Loway 12", "Highway 21")
        
        with connection.cursor() as cursor:
            cursor.execute(update_query, val)
            connection.commit()
            print(cursor.rowcount, "record(s) updated")

            # Select the updated records to verify the changes
            select_query = "SELECT name, address FROM customers WHERE address = %s"
            cursor.execute(select_query, ("Loway 12",))
            updated_records = cursor.fetchall()
            
            print("Updated Records:")
            for record in updated_records:
                print(record)
except Error as e:
    print(e)
