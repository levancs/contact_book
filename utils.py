def normalize_text(text):
    if not isinstance(text, str):
        return None
    text = text.strip()
    return text if text else None


def parse_integer(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None