# Third-party
from firecrawl import FirecrawlApp, ScrapeOptions
# Local imports
from utilities import load_api_key

class FirecrawlService:
    def __init__(self):
        self._initialize_llm()

    def _initialize_llm(self) -> None:
       try:
           api_key = load_api_key()
           self.app = FirecrawlApp(api_key=api_key)

       except Exception as e:
           ValueError(f"[FirecrawlService] Failed to initialize FirecrawlApp: {e}")

    def search_events(self, query: str, city: str):
        try:
            result = self.app.search(
                query=query,
                location=city,
                scrape_options=ScrapeOptions(formats=["markdown"])
            )

            return result
        except Exception as e:
            print(f"[FirecrawlService] Error during event search: {e}")
            return []

    def scrape_events_pages(self, url: str):
        try:
            result = self.app.scrape_url( url,formats=["markdown"])

            return result
        except Exception as e:
            print(f"[FirecrawlService] Error scraping URL '{url}': {e}")
            return None
