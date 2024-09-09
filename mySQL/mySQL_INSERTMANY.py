from getpass import getpass
from mysql.connector import connect, Error

# Values list
records = [
    ("Jotaro Kujo", "Stardust Road 12"),
    ("Joseph Joestar", "Ripple Street 34"),
    ("Dio Brando", "Vampire Lane 56"),
    ("Jonathan Joestar", "Hamon Bulevard 101"),
    ("Giorno Giovanna", "Golden Street 202")
]

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
            # Insert values
            db_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            
            total_records_inserted = 0
            
            for record in records:
                cursor.execute(db_query, record)
                connection.commit()  # Commit transaction
                total_records_inserted += cursor.rowcount
                print(f"Record inserted with ID: {cursor.lastrowid} - Name: {record[0]}, Address: {record[1]}")
            
            print("Total records inserted: ", total_records_inserted)

except Error as e:
    print(e)
