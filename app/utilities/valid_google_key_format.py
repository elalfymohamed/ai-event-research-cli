# Standard library
import re

def is_valid_google_key_format(key: str) -> bool:
    """ Google API keys usually start with "AIza" and are 39-40 characters long """

    if not isinstance(key, str) or not key:
        return False

    return bool(re.match(r'^AIza[0-9A-Za-z_-]{35,}$', key))
