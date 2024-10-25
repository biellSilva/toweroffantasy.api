def get_version() -> str:
    from pathlib import Path

    return Path("src/VERSION.txt").read_text(encoding="utf-8").strip()
