from database import get_connection
import psycopg.errors
from utils import validate_text


def add_contact(name, email):
    name = name.strip()
    email = email.strip()
    if not validate_text(name):
        return "invalid_input"
    if not validate_text(email):
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
    new_name = new_name.strip()
    if not validate_text(new_name):
        return "invalid_input"
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
            if cursor.rowcount == 0:
                return "contact_not_found"
            return "success"


def update_contact_email(contact_id, new_email):
    new_email = new_email.strip()
    if not validate_text(new_email):
        return "invalid_input"
    try:
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
                if cursor.rowcount == 0:
                    return "contact_not_found"
    except psycopg.errors.UniqueViolation:
        return "duplicate_email"
    return "success"


def update_contact_name_email(contact_id, new_name, new_email):
    new_name = new_name.strip()
    new_email = new_email.strip()
    if not validate_text(new_name):
        return "invalid_input"
    if not validate_text(new_email):
        return "invalid_input"
    try:
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
                if cursor.rowcount == 0:
                    return "contact_not_found"
    except psycopg.errors.UniqueViolation:
        return "duplicate_email"
    return "success"


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
            if cursor.rowcount == 0:
                return "contact_not_found"
            return "success"