from datetime import datetime
from re import search
from zoneinfo import ZoneInfo


def current_datetime() -> datetime:
    return datetime.now(ZoneInfo("America/Sao_Paulo"))


def truncate_value(value: float, precision: int = 2) -> int | float:
    """Truncate a float value to a specified number of decimal places.

    Args:
        value (float): The float value to truncate.
        precision (int): The number of decimal places to keep. Default is 2.

    Returns:
        float or int: The truncated value. If the truncated value is an integer,
            it will be returned as an int; otherwise, it will be returned as a float.
    """
    truncated_value = round(value, precision)
    return (
        int(truncated_value)
        if truncated_value == int(truncated_value)
        else truncated_value
    )


def needs_translation(string: str) -> bool:
    """Check if a string needs translation.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string needs translation, False otherwise.
    """

    # Matches optional namespace followed by a key
    pattern = r"^(?:[A-Za-z0-9_]+)?\.[A-Za-z0-9_\-]+$"
    return bool(search(pattern, string))


def needs_values(string: str) -> bool:
    """Check if a string needs values.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string needs values, False otherwise.
    """

    # Matches placeholders like {0}, {1}, etc.
    pattern = r"\{[0-9]+\}"
    return bool(search(pattern, string))
