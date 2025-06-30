#!/bin/bash

# AI Event Research CLI - Project Runner Script

# Exit immediately on error
set -e

CITY=${1:cairo}
TOPIC=${2:software}
APY_KEY=${3:-""} # Optional

echo "🚀 Running AI Event Research CLI"
echo "📍 City: $CITY"
echo "📌 Topic: $TOPIC"
if [ -n "$API_KEY" ]; then
    echo "🔑 Using provided API Key"
fi

if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
else
    echo "⚠️ Python 3 not found. Trying default 'python'..."
    PYTHON_CMD="python"
fi


if [ -d ".venv" ]; then
    echo "💡 Activating virtual environment..."
    if [[ "$OSTYPE" == "darwin"* || "$OSTYPE" == "linux-gnu"* ]]; then
           source .venv/bin/activate
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
           source .venv/Scripts/activate
    fi
fi

cd ./app || { echo "❌ 'app' directory not found!"; exit 1; }

if [ -n "$API_KEY" ]; then
    python main.py --city="$CITY" --topic="$TOPIC" --key="$API_KEY"
else
    python main.py --city="$CITY" --topic="$TOPIC"
fi

echo "✅ Done! Check the generated Excel file."
