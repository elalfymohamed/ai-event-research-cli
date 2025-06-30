# Standard library
import re

def is_valid_firecrawl_key_format(key: str) -> bool:
    """ Firecrawl API keys usually start with "fc-" and are 32-40 characters long """
    if not isinstance(key, str) or not key:
        return False
    return bool(re.match(r'^fc-[0-9A-Za-z_-]{32,}$', key))
