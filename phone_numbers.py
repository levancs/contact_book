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