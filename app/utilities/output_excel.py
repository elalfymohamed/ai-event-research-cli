# Third-party
import pandas as pd

# Standard library
from pathlib import Path
from datetime import datetime
from typing import  Any

# Local imports
from config.logging_config import setup_logger

logger = setup_logger()

def output_excel(input: dict, output:  dict[str, Any]) -> None:
    path_dir = Path(__file__).resolve().parent.parent.parent / "events"
    path_dir.mkdir(parents=True, exist_ok=True)

    topic = input.get("topic", "events").replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = path_dir / f"{topic}_output_{timestamp}.csv"

    try:
        df = pd.DataFrame(output)
        df.to_csv(file_path, index=False)
        logger.info(f"✅ Output written to: {file_path}")
    except Exception as e:
        logger.error(f"❌ Failed to write output file: {e}")
        raise
