# Third-party
import pandas as pd

# Standard library
from pathlib import Path
from datetime import datetime
from typing import Any

# Local imports
from config.logging_config import setup_logger

logger = setup_logger()

URLS_FILENAME = "urls.txt"
EXCEL_FILENAME = "events.xlsx"

class Output:
    def __init__(self, input: dict[str, Any], urls: list[str], output: list[dict[str, Any]]):
        logger.info("📁 Initializing Output class for event export.")
        self.path_dir = Path(__file__).resolve().parent.parent.parent / "events"
        self.folder_path = None
        self.urls = urls
        self.output = output
        self._create_folder(input)
        self._initialize_output()

    def _create_folder(self, input: dict):
        self.path_dir.mkdir(parents=True, exist_ok=True)
        topic = input.get("topic", "events").replace(" ", "_").lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        foldername_prefix = f"{topic}_output_{timestamp}"
        self.folder_path = self.path_dir / foldername_prefix
        self.folder_path.mkdir(parents=True, exist_ok=True)


    def _initialize_output(self):
        self._urls_txt()
        self._event_excel()
        logger.info(f"📦 All outputs saved in: {self.folder_path}")

    def _urls_txt(self):
        if self.folder_path is None:
            raise ValueError("File path not initialized. Call _create_folder() first.")
        txt_path =  Path(self.folder_path) / URLS_FILENAME

        try:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(self.urls))
            logger.info(f"✅ URLs written to: {txt_path}")
        except Exception as e:
            logger.error(f"❌ Failed to write URLs file: {e}")
            raise

    def _event_excel(self) -> None:
        if self.folder_path is None:
            raise ValueError("File path not initialized. Call _create_folder() first.")
        xlsx_path =   Path(self.folder_path) / EXCEL_FILENAME

        try:
            df = pd.DataFrame(self.output)
            df.to_excel(xlsx_path, index=False)
            logger.info(f"✅ Excel output written to: {xlsx_path}")
        except Exception as e:
            logger.error(f"❌ Failed to write Excel output: {e}")
            raise
