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

def get_contacts():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * 
        FROM contacts;
        """
    )

    contacts = cursor.fetchall()

    cursor.close()
    connection.close()

    return contacts  

def update_contact_name(contact_id, new_name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE contacts
        SET name = %s
        WHERE contact_id = %s
        """,
        (new_name, contact_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

def update_contact_email(contact_id, new_email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE contacts
        SET email = %s
        WHERE contact_id = %s
        """,
        (new_email, contact_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

def update_contact_name_email(contact_id, new_name, new_email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE contacts
        SET name = %s, email = %s
        WHERE contact_id = %s
        """,
        (new_name, new_email, contact_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

def delete_contact(contact_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM contacts
        WHERE contact_id = %s
        """,
        (contact_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()