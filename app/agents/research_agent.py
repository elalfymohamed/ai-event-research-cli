# Standard library
from typing import Union, Any, Dict, List
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Third-party
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# Local imports
from config import setup_logger, AgentConfig
from utilities import output_excel
from helpers import ResearchPromo
from models import ResearchState, EventInfo
from .firecrawl import FirecrawlService


logger = setup_logger()

class ResearchAgent:
    """
    Agent for conducting topics-based research using AI.
    """

    def __init__(self, months: int = 1):
        self.config = AgentConfig()
        self.firecrawl = FirecrawlService()
        self.prompts = ResearchPromo()
        self._initialize_llm()
        self.graph = self._build_graph()
        self.months = months



    def _initialize_llm(self) -> None:
        """
        Initialize the loacal AI model using loaded API key and configuration.
        """
        try:

            self.llm = ChatOllama(
                model=self.config.model,
                temperature=self.config.temperature,
                top_p=self.config.top_p,
                top_k=self.config.top_k,
                )

            logger.info(f"✅ LLM initialized with model: {self.config.model}")

        except Exception as e:
           raise ValueError(f"❌ Failed to initialize LLM: {e}")


    def _research_node(self, state: ResearchState) -> Dict[str, Any]:
        """
        Node function for the LangGraph: searches for event content and scrapes pages using Firecrawl.
        """
        try:
            logger.info("🔍 Starting research node...")

            city = state.city
            topics = state.topic

            logger.info(f"📍 Location: {city} | 🔖 Topic: {topics}")

            date_now = datetime.now()
            start_date = date_now.strftime("%Y-%m-%d")
            end_date = (date_now + relativedelta(months=self.months)).strftime("%Y-%m-%d")

            logger.info("🛠 Creating query prompt...")
            query = f"List upcoming {topics} events in {city} between {start_date} and {end_date}. Include name, description, location, date, and link."
            
            logger.info(f"🛠 Creating query for date range {start_date} to {end_date}")

            logger.info("🔎 Querying Firecrawl search...")
            search_results = self.firecrawl.search_events(query=query, city=city)

            if not search_results or not hasattr(search_results, "data"):
                raise ValueError("❌ No search results returned from Firecrawl")

            logger.info(f"✅ Found {len(search_results.data)} results. Starting scrape...")

            all_content = []
            for result in search_results.data:
                url = result.get("url")
                if not url:
                    logger.warning("⚠️ Missing URL in search result, skipping.")
                    continue

                logger.info("🔎 Research ...")
                logger.info(f"🌐 Scraping: {url}")
                scraped = self.firecrawl.scrape_events_pages(url)
                if scraped:
                    try:
                        all_content.append({
                            "url": url,
                           "content": str(scraped)
                        })
                    except Exception as conv_err:
                        logger.warning(f"⚠️ Could not convert scrape result for {url}: {conv_err}")

            logger.info(f"✅ Completed scraping {len(all_content)} pages.")

            return { "search_results": all_content }

        except Exception as e:
            raise ValueError(f"❌ Error during research node: {str(e)}")

    def _analyze_events_content(self, content: str, source_url: str) -> Union[List[EventInfo], List]:
        structured_llm = self.llm.with_structured_output(EventInfo)

        messages = [
            SystemMessage(content=self.prompts.EVENT_ANALYSIS_SYSTEM),
            HumanMessage(content=self.prompts.event_analysis_content(content=content, source_url=source_url))
        ]

        try:
            logger.info(f"🔍 Analyzing content from: {source_url}")

            result = structured_llm.invoke(messages)

            return result


        except Exception as e:
            logger.warning(f"❌ LLM analysis failed for {source_url}: {str(e)}")
            return []

    def _analyze_research_results(self, state: ResearchState) -> Dict[str, Any]:
        """
        Analyzes scraped web pages and extracts structured event data.
        """
        try:
            logger.info("🧠 Starting LLM event analysis...")

            all_events = []

            for page in state.search_results:
                content = page.get("content")
                url = page.get("url")

                if not content or not url:
                    continue

                events = self._analyze_events_content(content=content, source_url=url)

                all_events.extend(events)

            logger.info(f"✅ Extracted {len(all_events)} events.")
            return { "events": all_events, "search_results": [] }

        except Exception as e:
            logger.error(f"❌ Error analyzing scraped pages: {str(e)}")
            return { "events": [] }

    def _build_graph(self):
        """
        Builds the LangGraph execution flow for event research.
        """
        graph = StateGraph(ResearchState)

        graph.add_node("research", self._research_node)

        graph.add_node("analyze", self._analyze_research_results)

        graph.set_entry_point("research")
        graph.add_edge("research", "analyze")
        graph.add_edge("analyze", END)

        compiled_graph = graph.compile()
        logger.info("✅ Research graph compiled successfully")
        return compiled_graph


    def run_research(self, topic: str, city: str):
        """
        Runs the graph with given input parameters.
        """
        try:
            state = ResearchState(topic=topic, city=city)

            result = self.graph.invoke(state)

            final_output = result.get("events") or result

            output_excel(input={"topic": topic} ,output=final_output)

        except Exception as e:
            raise ValueError(f"❌ Error during research execution: {str(e)}")
