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
        with connection.cursor() as cursor:
            # Describe table
            describe_query = "DESCRIBE customers"
            cursor.execute(describe_query)
            
            print("Current Table Structure:")
            for row in cursor.fetchall():
                print(row)
            
            add_column_query = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST"
            cursor.execute(add_column_query)
            
            # Commit the changes
            connection.commit()
            
            # Describe the table again to verify changes
            cursor.execute(describe_query)
            print("\nUpdated Table Structure:")
            for row in cursor.fetchall():
                print(row)

except Error as e:
    print(f"Error: {e}")
