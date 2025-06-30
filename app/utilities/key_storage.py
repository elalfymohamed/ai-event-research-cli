# Standard library
import os
from pathlib import Path

# Local imports
from utilities import is_valid_firecrawl_key_format
from constants.keys import FILE_KEY_NAME
from config import setup_logger

logger = setup_logger()

class KeyStorage:
    def __init__(self, key: str | None):
        self.file_name = FILE_KEY_NAME
        self.path_file = Path(__file__).resolve().parent.parent.parent / self.file_name
        self._initialize_key(key)

    def _initialize_key(self, key: str | None) -> None:
        """Create the key file if it doesn't exist."""
        if not self._is_file_exists() and key:
            self._create_file_key(key)

    def _create_file_key(self, key: str) -> None:
        """Write the given key to the file and secure its permissions."""
        try:
            with open(self.path_file, "w") as f:
                f.write(key)
            os.chmod(self.path_file, 0o600)
            logger.info("✅ The key file was created successfully.")
        except Exception as e:
            raise ValueError(f"Failed to write key to file '{self.file_name}': {e}")

    def _is_file_exists(self) -> bool:
        """Check if the key file already exists."""
        return os.path.exists(self.path_file)

    def get_value_key(self) -> str:
        """ Retrieve and validate the stored key """
        if not self._is_file_exists():
            raise ValueError(
                f"❌ The key file '{self.file_name}' does not exist.\n"
                "🔐 You can add the key in a `.env` file or provide it using the `--key` flag when running the command."
            )

        try:
            with open(self.path_file, "r") as f:
                content = f.readline().strip()

                if not content:
                    raise ValueError("⚠️ The key file is empty.")

                if not is_valid_firecrawl_key_format(content):
                    raise ValueError("❗ The key format is invalid.")

                logger.info("✅ API key loaded from file successfully.")
                return content

        except Exception as e:
            raise ValueError(f"🚫 Failed to read key from file '{self.file_name}': {e}")
