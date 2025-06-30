# Local imports
from utilities import is_valid_firecrawl_key_format

class ValidationError(Exception):
    pass


def validate_required_args(args: dict) -> None:
    """
    Validates parsed arguments from docopt.
    Exits the program with an error message if validation fails.
    """
    topic = args.get("--topic")
    city = args.get("--city")
    key = args.get("--key")

    # Validate --topic
    if not topic:
        raise ValidationError("❌ --topics is required.")

    # Validate --city
    if not city:
        raise ValidationError("❌  --city must be comma-separated values with no spaces.")

    # Validate --key
    if key and not is_valid_firecrawl_key_format(key):
        raise ValidationError("❌ Invalid Firecrawl API key format.")
