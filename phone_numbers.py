from database import get_connection
import psycopg.errors
from utils import validate_text


def add_phone_number(contact_id, number, phone_type):
    number = number.strip()
    phone_type = phone_type.strip()
    if not validate_text(number):
        return "invalid_input"
    if not validate_text(phone_type):
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
    new_number = new_number.strip()
    new_phone_type = new_phone_type.strip()
    if not validate_text(new_number):
        return "invalid_input"
    if not validate_text(new_phone_type):
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
            if cursor.rowcount == 0:
                return "phone_number_not_found"
            return "success"


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
            if cursor.rowcount == 0:
                return "phone_number_not_found"
            return "success"