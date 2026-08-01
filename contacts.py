from database import get_connection
import psycopg.errors


def validate_contact(name, email):
    if not name.strip():
        return False
    if not email.strip():
        return False
    return True


def add_contact(name, email):
    if not validate_contact(name, email):
        return "invalid_input"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                        """
                        INSERT INTO contacts(name, email)
                        VALUES (%s, %s)
                        """,
                        (name, email)
                    )
    except psycopg.errors.UniqueViolation:
        return "duplicate_email"
    except psycopg.errors.NotNullViolation:
        return "missing_required_field"
    return "success"


def get_contacts():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT contact_id, name, email 
                FROM contacts;
                """
            )
            contacts = cursor.fetchall()
            return contacts
  

def update_contact_name(contact_id, new_name):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE contacts
                SET name = %s
                WHERE contact_id = %s
                """,
                (new_name, contact_id)
            )


def update_contact_email(contact_id, new_email):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE contacts
                SET email = %s
                WHERE contact_id = %s
                """,
                (new_email, contact_id)
            )


def update_contact_name_email(contact_id, new_name, new_email):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE contacts
                SET name = %s, email = %s
                WHERE contact_id = %s
                """,
                (new_name, new_email, contact_id)
            )


def delete_contact(contact_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM contacts
                WHERE contact_id = %s
                """,
                (contact_id,)
            )
                