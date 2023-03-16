import os


def getenv_bool(key: str) -> bool:
    return bool(os.getenv(key).capitalize())
