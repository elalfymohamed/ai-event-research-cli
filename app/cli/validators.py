# Local imports
from utilities import is_valid_google_key_format

class ValidationError(Exception):
    pass


def validate_required_args(args: dict) -> None:
    """
    Validates parsed arguments from docopt.
    Exits the program with an error message if validation fails.
    """
    topics = args.get("--topics")
    city = args.get("--city")
    country = args.get("--country")
    key = args.get("--key")

    # Validate --topics
    if not topics:
        raise ValidationError("❌ --topics is required.")

    # Validate --city
    if not city:
        raise ValidationError("❌  --city must be comma-separated values with no spaces.")

    # Validate --country (single word only)
    if country and (',' in country or ' ' in country.strip()):
        raise ValidationError("❌ --country must be a single word (no commas or spaces).")

    # Validate --key
    if key and not is_valid_google_key_format(key):
        raise ValidationError("❌ Invalid Google API key format.")
