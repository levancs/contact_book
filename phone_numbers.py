import psycopg.errors
from database import get_connection
from utils import normalize_text


def add_phone_number(contact_id, number, phone_type):
    number = normalize_text(number)
    phone_type = normalize_text(phone_type)
    if number is None or phone_type is None:
        return "invalid_input"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO phone_numbers(contact_id, number, type)
                    VALUES (%s, %s, %s)
                    """,
                    (contact_id, number, phone_type)
                )
    except psycopg.errors.ForeignKeyViolation:
        return "contact_not_found"
    except psycopg.errors.UniqueViolation:
        return "duplicate_phone_number"
    return "success"


def get_phone_numbers(contact_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT phone_id, number, type
                FROM phone_numbers
                WHERE contact_id = %s
                """,
                (contact_id,)
            )
            phone_numbers = cursor.fetchall()
            return phone_numbers


def update_phone_number(phone_id, new_number, new_phone_type):
    new_number = normalize_text(new_number)
    new_phone_type = normalize_text(new_phone_type)
    if new_number is None or new_phone_type is None:
        return "invalid_input"
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE phone_numbers
                SET number = %s, type = %s
                WHERE phone_id = %s
                """,
                (new_number, new_phone_type, phone_id)
            )
            return "phone_number_not_found" if cursor.rowcount == 0 else "success"


def delete_phone_number(phone_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM phone_numbers
                WHERE phone_id = %s
                """,
                (phone_id,)
            )
            return "phone_number_not_found" if cursor.rowcount == 0 else "success"