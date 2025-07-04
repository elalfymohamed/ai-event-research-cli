# Third-party
from dotenv import load_dotenv
# Standard library
from pathlib import Path
import os
# Local imports
from . import is_valid_firecrawl_key_format, KeyStorage
from constants.keys import VARIABLE_KEY_ENV
from config import setup_logger

logger = setup_logger()

def load_api_key() -> str:
    """ Load the API key from the .env file or fallback to the key file """
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"

    load_dotenv(env_path)

    api_key = os.getenv(VARIABLE_KEY_ENV)

    if api_key and is_valid_firecrawl_key_format(api_key):
        logger.info("✅ Firecrawl API key loaded from .env successfully.")
        return api_key

    else:
        logger.warning("⚠️ Environment variable not found or invalid. Falling back to key file...")
        file_key = KeyStorage(key=None).get_value_key()

        return file_key
