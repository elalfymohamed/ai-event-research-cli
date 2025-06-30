# Third-party
from docopt import docopt
# Standard library
import sys
# Local imports
from cli import USAGE, validate_required_args
from utilities import KeyStorage
from config import setup_logger
from agents.research_agent import ResearchAgent


logger = setup_logger()

def main():
    """ CLI entrypoint for event research using AI """
    try:
        args = docopt(USAGE)
        validate_required_args(args)

        topic = args.get("--topic")
        city = args.get("--city")
        api_key = args.get("--key")

        if api_key:
            KeyStorage(api_key)

        logger.info("🚀 Starting research agent")
        agent = ResearchAgent()
        agent.run_research(topic=topic, city=city)

        print("🎯 Final Output")

    except Exception as e:
        logger.error(e)
        sys.exit(1)



if __name__ == '__main__':
    """
    How to run:
        Mac/Linux -> python main.py --city=cairo --topic=software
        Windows   -> py main.py --city=cairo --topic=software

    To get help, run:
        Mac/Linux -> python main.py -h
        Windows   -> py main.py -h
    """
    main()
