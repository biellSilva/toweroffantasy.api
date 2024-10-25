from datetime import datetime
from zoneinfo import ZoneInfo


def current_datetime() -> datetime:
    return datetime.now(ZoneInfo("America/Sao_Paulo"))
