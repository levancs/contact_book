import psycopg.errors
from database import get_connection
from utils import normalize_text


def add_contact(name, email):
    name = normalize_text(name)
    email = normalize_text(email)
    if name is None or email is None:
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


def get_contacts_descriptive():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    contacts.contact_id,
                    contacts.name,
                    contacts.email,
                    phone_numbers.phone_id,
                    phone_numbers.number AS phone_number,
                    phone_numbers.type AS phone_type,
                    tags.tag_id,
                    tags.name as tag_name
                FROM contacts
                LEFT JOIN phone_numbers
                    ON contacts.contact_id = phone_numbers.contact_id
                LEFT JOIN contact_tags
                    ON contacts.contact_id = contact_tags.contact_id
                LEFT JOIN tags
                    ON contact_tags.tag_id = tags.tag_id
                """
            )
            descriptive_contacts = cursor.fetchall()
            return descriptive_contacts

        
def update_contact_name(contact_id, new_name):
    new_name = normalize_text(new_name)
    if new_name is None:
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
            return "contact_not_found" if cursor.rowcount == 0 else "success"


def update_contact_email(contact_id, new_email):
    new_email = normalize_text(new_email)
    if new_email is None:
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
                rowcount = cursor.rowcount
    except psycopg.errors.UniqueViolation:
        return "duplicate_email"
    return "contact_not_found" if rowcount == 0 else "success"


def update_contact_name_email(contact_id, new_name, new_email):
    new_name = normalize_text(new_name)
    new_email = normalize_text(new_email)
    if new_name is None or new_email is None:
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
                rowcount = cursor.rowcount
    except psycopg.errors.UniqueViolation:
        return "duplicate_email"
    return "contact_not_found" if rowcount == 0 else "success"


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
            return "contact_not_found" if cursor.rowcount == 0 else "success"