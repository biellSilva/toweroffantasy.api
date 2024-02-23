def weapon_effect_title(text: str) -> str:
    if text and text.endswith(":"):
        return text.replace(":", "").replace("*", "")
    return text
