from getpass import getpass
from mysql.connector import connect, Error

# Get user credentials
username = input("Enter username: ")
password = getpass("Enter password: ")

# List of tuples values for users
records = [
    ("Jotaro", 1 ),
    ("Joseph", 1 ),
    ("Jolyne", 2 ),
    ("Jonathan", None ),
    ("Giorno", 3)
]

# List of products
records2 = [
    "Chocolate Heaven",
    "Tasty Lemons",
    "Vanilla Dreams",
    "Strawberry Shake"
]

try:
    with connect(
        host="localhost",
        user=username,
        password=password,
    ) as connection:
        # Create database
        create_db_query = "CREATE DATABASE IF NOT EXISTS food_preference"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        print("Database created successfully or already exists")

        # Show databases
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
        
        # Select the database
        use_db_query = "USE food_preference"
        with connection.cursor() as cursor:
            cursor.execute(use_db_query)
    
        # Create tables
        table_db_query = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), favorite INT)"
        with connection.cursor() as cursor:
            cursor.execute(table_db_query)
            
        table_db_query = "CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
        with connection.cursor() as cursor:
            cursor.execute(table_db_query)
            
        # Show table(s)
        show_table_db_query = "SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(show_table_db_query)
            for x in cursor:
                print(x)
                
        #Insert values
        insert_query = "INSERT INTO users (name, favorite) VALUES (%s, %s)"
        with connection.cursor() as cursor:
            cursor.executemany(insert_query, records)
            connection.commit()
            print(cursor.rowcount, "value(s) were inserted in 'users'")
            
        insert_query = "INSERT INTO products (name) VALUES (%s)"
        with connection.cursor() as cursor:
            for product in records2:
                cursor.execute(insert_query, (product, ))
            connection.commit()
            print(len(records2), "value(s) were inserted in 'products'")
            
        # Print inserted values from users table
        select_users_query = "SELECT * FROM users"
        with connection.cursor() as cursor:
            cursor.execute(select_users_query)
            users = cursor.fetchall()
            print("Inserted values in 'users' table:")
            for user in users:
                print(user)

        # Print inserted values from products table
        select_products_query = "SELECT * FROM products"
        with connection.cursor() as cursor:
            cursor.execute(select_products_query)
            products = cursor.fetchall()
            print("Inserted values in 'products' table:")
            for product in products:
                print(product)       
except Error as e:
    print(f"Error: {e}")
