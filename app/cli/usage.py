USAGE = """
Events Search

Usage:
  main.py [--city=<city>] --topic=<topic> [--country=<country>] [--months=<months>] [--key=<key>]
  main.py -h | --help

Options:
  --city=<city>       Optional city name [default: cairo]. You can specify multiple cities separated by commas.
  --topic=<topic>     Required topic name(s) (e.g., software, market).
  --country=<country> Optional country name [default: eg]. country code (e.g., eg, us). Only one country is allowed.
  --months=<months>   Optional months name [default: 1]. Number of months to search for events starting from today. Minimum is 1, maximum is 4.
  --key=<key>         Optional  Firecrawl API key for web data extraction.
  -h --help           Show this help message.

Description:
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ 💬 This project utilizes ✨ Ollama AI ✨ and ✨ Firecrawl ✨ to        │
  │ intelligently retrieve, summarize, and structure event information based   │
  │ on specific cities and given topics.                                       │
  │                                                                            │
  │ It gathers event names, descriptions, locations, and links —               │
  │ then generates an Excel file to organize the collected data.               │
  │                                                                            │
  │ 🔧 Example command:                                                        │
  │     main.py --city=cairo --topic=software --months=2                       │
  │      --country=eg --key=your-firecrawl-api-key                             │
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
