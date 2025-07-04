# Local imports
from utilities import is_valid_firecrawl_key_format

class ValidationError(ValueError):
    pass

def validate_required_args(args: dict) -> None:
    """
    Validates parsed arguments from docopt.
    Exits the program with an error message if validation fails.
    """
    topic = args.get("--topic")
    city = args.get("--city")
    months = args.get("--months")
    key = args.get("--key")

    # Validate --topic
    if not topic:
        raise ValidationError("❌ --topics is required.")

    # Validate --city
    if not city:
        raise ValidationError("❌  --city must be comma-separated values with no spaces.")
    
    # Validate --months
    if months:
        try:
            months = int(months)
        except (TypeError, ValueError):
            raise ValidationError("❌ --months must be an integer between 1 and 4.")
        
        if int(months) < 1 or int(months) > 4:
            raise ValidationError("❌ --months must be between 1 and 4 for get best .")

    # Validate --key
    if key and not is_valid_firecrawl_key_format(key):
        raise ValidationError("❌ Invalid Firecrawl API key format.")

