def get_version() -> str:
    from pathlib import Path

    version_file = Path("src/VERSION.txt")

    if not version_file.is_file():
        return "0.0.0"

    return version_file.read_text(encoding="utf-8").strip()
