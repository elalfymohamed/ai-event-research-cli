USAGE = """
Smart Event

Usage:
  main.py [--city=<city>] [--country=<country>] --topics=<topics> [--key=<key>]
  main.py -h | --help

Options:
  --city=<city>        Optional city name [default: cairo]. You can specify multiple cities separated by commas.
  --country=<country>  Optional country name (only one country allowed).
  --topics=<topics>      Required topics name (e.g., software, market, etc.).
  --key=<key>          Optional Google API key for Gemini (GEMINI) AI access.
  -h --help            Show this help message.

Description:
  ┌───────────────────────────────────────────────────────────────┐
  │ 💬 This project utilizes ✨ Gemini AI ✨ to intelligently     │
  │ retrieve, summarize, and structure event information based    │
  │ on specific cities or countries and a given topics.           │
  │ It gathers event names, descriptions, locations, and links —  │
  │ then generates an Excel file to organize the collected data.  │
  │                                                               │
  │ 🔧 Example command:                                           │
  │     main.py --city=cairo --country=egypt                      │
  │             --topics=software --key=your-google-api-key       │
  │                                                               │
  │ 🔑 How to Get a Google API Key:                               │
  │   1. Visit: https://aistudio.google.com/app/apikey            │
  │   2. Sign in and create an API key                            │
  │   3. Copy the generated key                                   │
  └───────────────────────────────────────────────────────────────┘
"""
