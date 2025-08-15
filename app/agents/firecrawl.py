# Third-party
from firecrawl import FirecrawlApp, ScrapeOptions
# Local imports
from utilities import load_api_key
from models import ResultFirecrawl
from config import setup_logger

logger = setup_logger()

class FirecrawlService:
    def __init__(self):
        self._initialize_llm()

    def _initialize_llm(self) -> None:
       try:
           api_key = load_api_key()
           self.app = FirecrawlApp(api_key=api_key)

       except Exception as e:
           ValueError(f"[FirecrawlService] Failed to initialize FirecrawlApp: {e}")

    def search_events(self, query: str, city: str, country: str) -> ResultFirecrawl:
        """
        Searches for events using the Firecrawl app based on query and location.
        """
        try:
            result = self.app.search(
                query=query,
                location=city,
                scrape_options=ScrapeOptions(formats=["markdown"]),
                limit=30,
                country=country
            )
            return result

        except Exception as e:
            logger.error(f"[FirecrawlService] Error during event search: {e}")
            return ResultFirecrawl(data=[])

    def scrape_events_pages(self, url: str):
        try:
            result = self.app.scrape_url(url,formats=["markdown"], block_ads=True)

            return result
        except Exception as e:
            logger.error(f"[FirecrawlService] Error scraping URL '{url}': {e}")
            return None
