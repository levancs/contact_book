import psycopg

connection = psycopg.connect(
    dbname="contact_book_db",
    user="postgres",
    password="Work123Elikashvili123*",
    host="localhost",
    port=5432
)

print("Connection Successful")

connection.close()