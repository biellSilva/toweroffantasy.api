def weapon_matrix_rework(id: str) -> str | None:
    if id.lower() in ("none", "null"):
        return None
    return id.lower()


def voice_actor_rework(actor: str) -> str:
    return actor.removeprefix(" ")
