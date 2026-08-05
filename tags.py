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


def get_tags():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute (
                """
                SELECT tag_id, name
                FROM tags
                """
            )
            tags = cursor.fetchall()
            return tags


def assign_tag(contact_id, tag_id):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute (
                    """
                    INSERT INTO contact_tags(contact_id, tag_id)
                    VALUES (%s, %s)
                    """,
                    (contact_id, tag_id)
                )
    except psycopg.errors.ForeignKeyViolation:
        return "contact_or_tag_not_found"
    except psycopg.errors.UniqueViolation:
        return "tag_already_assigned"
    return "success"


def delete_tag(tag_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute (
                """
                DELETE FROM tags
                WHERE tag_id = %s
                """,
                (tag_id,)
            )
            return "tag_not_found" if cursor.rowcount == 0 else "success"