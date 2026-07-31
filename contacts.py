from database import get_connection

def add_contact(name, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO contacts(name, email)
        VALUES (%s, %s)
        """,
        (name, email)
    )

    connection.commit()

    cursor.close()
    connection.close()