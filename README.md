# 🧠 AI Event Research CLI
<p align="center">
<img width="982" height="472" alt="Image" src="https://github.com/user-attachments/assets/c4b91df7-4072-49e8-9f01-5a3f652d31ee" />
</p>

## 🔍 What is this?

This CLI tool uses a local LLM model with LangGraph, LangChain, and Firecrawl to search, analyze, and extract structured information about upcoming events based on location and topic.

This project leverages ✨ **Ollama AI (Local LLM)** ✨ and ✨ **Firecrawl** ✨ to intelligently retrieve, summarize, and structure event information based on specific cities and topics — **entirely on your machine**, with no OpenAI or cloud LLM usage required.

---

## 🌟 Overview

The **AI Event Research CLI** is designed to streamline the process of finding and analyzing information about upcoming events. By combining the power of local Large Language Models (LLMs) with advanced web scraping and data extraction techniques, it provides a robust solution for:

- Researchers
- Event organizers
- Anyone interested in staying informed about industry-specific events

---

## 📦 Features

- 🔍 **Event Querying**: Search for upcoming conferences, webinars, and expos based on location and topic.
- 🌐 **Web Scraping with Firecrawl**: Uses Firecrawl to scrape relevant event web pages.
- 🧠 **LLM-Powered Analysis**: Utilizes Ollama + LangChain to analyze and extract event data.
- 📊 **Structured Data Extraction**: Pydantic models ensure reliable and consistent formatting.
- 📈 **Excel Export**: Automatically exports final results to Excel.
- 🔐 **Secure API Key Storage**: Manage your Firecrawl API key securely.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/elalfymohamed/ai-event-research-cli.git
cd ai-event-research-cli
```

## 🧠 Using Ollama Locally

- This project relies on <a href="https://ollama.com/" target="_blank">Ollama</a> to run LLMs locally.

### ✅ Requirements

- Install <a href="https://ollama.com/" target="_blank" >Ollama</a>

- Pull a model of your choice (e.g. llama3, mistral, gemma, etc.)

```bash
ollama run llama3
```

## 🔑 How to Get a Firecrawl API Key

1. Visit: <https://www.firecrawl.dev/app>
2. Sign in and create an API key
3. Copy the scraping key

## Install Dependencies

Next, install all the necessary Python packages using pip:

```bash
python3 -m venv .venv

#Linux / macOS:
source .venv/bin/activate
#Windows:
.venv/Scripts/activate

pip install -r requirements.txt
```

### 3. Run the CLI Tool

You can run the CLI tool from your terminal.

```bash

#For Linux / macOS:

python main.py --city=cairo --topic=software

#For Windows:

py main.py --city=cairo --topic=software

```

## 🏃‍♂️ Run via Bash Script

You can run the tool with:

```bash
chmod +x run_project.sh

# Usage: ./run_project.sh <city> <topic> <country> <months> [api_key]
./run_project.sh cairo software eg 2 your_firecrawl_api_key

```

### 🔐 Using Environment Variables

To avoid passing your API key on the command line, create a `.env` file in the project root:

```bash
# .env
FIRECRAWL_API_KEY=your_api_key_here
```

The application will automatically load the key if not explicitly provided via --key.

## ⚙️ CLI Usage

The main.py script accepts several command-line arguments to customize your event search.

```bash
main.py [--city=<city>] --topic=<topic> [--country=<country>] [--months=<months>] [--key=<API_KEY>]

Options:

    --city=<city>: Optional. You can specify multiple cities separated by commas.
        Default: cairo
        Example: --city=cairo

    --topic=<topic>: Required. Define the target event topic (e.g., AI, Software, Cybersecurity).
        Example: --topic=software

    --country=<country> Optional. Specify a country code (e.g., eg, us). Only one country code allowed.
        Default: eg
        Example: --country=eg

    --months=<months>: Optional. Specify the number of months to search for events starting from the current date. Minimum is 1 month, maximum is 4 months.
         Default: 1
         Example: --months=2

    --key=<API_KEY>: Optional. Provide your API key for Firecrawl. If not provided, the tool will attempt to use a key in .env file.
        Example: --key=your_firecrawl_api_key_here

    -h, --help: Show this help message and exit.

```

## 🤝 Contributing

We welcome contributions! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.
