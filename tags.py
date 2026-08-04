import psycopg.errors
from database import get_connection
from utils import normalize_text


def add_tag(name):
    name = normalize_text(name)
    if name is None:
        return "invalid_input"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute (
                    """
                    INSERT INTO tags(name)
                    VALUES (%s)
                    """,
                    (name,)
                )
    except psycopg.errors.UniqueViolation:
        return "duplicate_tag"
    return "success"     