def validate_text(text):
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    return True


def validate_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False