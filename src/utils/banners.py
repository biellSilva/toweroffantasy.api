from datetime import datetime


def str_to_datetime(text: str) -> datetime:
    if ":" in text:
        return datetime.strptime(text, "%Y/%m/%d %H:%M")
    else:
        return datetime.strptime(text, "%Y/%m/%d")
