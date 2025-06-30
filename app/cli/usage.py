USAGE = """
Events Search

Usage:
  main.py [--city=<city>] --topic=<topic> [--key=<key>]
  main.py -h | --help

Options:
  --city=<city>        Optional city name [default: cairo]. You can specify multiple cities separated by commas.
  --topic=<topic>    Required topic names (e.g., software, market, etc.).
  --key=<key>          Optional Firecrawl API key for Firecrawl LLM access.
  -h --help            Show this help message.

Description:
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ 💬 This project utilizes ✨ Ollama AI ✨ and ✨ Firecrawl LLM ✨ to        │
  │ intelligently retrieve, summarize, and structure event information based   │
  │ on specific cities and given topics.                                       │
  │                                                                            │
  │ It gathers event names, descriptions, locations, and links —               │
  │ then generates an Excel file to organize the collected data.               │
  │                                                                            │
  │ 🔧 Example command:                                                        │
  │     main.py --city=cairo --topics=software --key=your-firecrawl-api-key    │
  │                                                                            │
  │ 🔑 How to Get a Firecrawl API Key:                                         │
  │   1. Visit: https://www.firecrawl.dev/app                                  │
  │   2. Sign in and create an API key                                         │
  │   3. Copy the scraping key                                                 │
  │                                                                            │
  │ 🧠 How to Install Local AI (Ollama):                                       │
  │   1. Visit: https://ollama.com                                             │
  │   2. Download and install for your OS                                      │
  │      - macOS: Follow the macOS installation guide                          │
  │      - Windows: Follow the Windows setup instructions                      │
  └────────────────────────────────────────────────────────────────────────────┘
"""
