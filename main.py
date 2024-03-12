if __name__ == "__main__":
    import os

    CMDS = [
        "python -m pip install pdm",
        "python -m pdm install",
        "python -m pdm run prod",
    ]

    for cmd in CMDS:
        os.system(cmd)
