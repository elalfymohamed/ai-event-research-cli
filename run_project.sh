#!/bin/bash

# AI Event Research CLI - Project Runner Script

# Exit immediately on error
set -e


CITY=${1:-cairo}
TOPIC=${2:-software}
API_KEY=${3:-""}  # Optional


echo "🚀 Running AI Event Research CLI"
echo "📍 City: $CITY"
echo "📌 Topic: $TOPIC"
if [ -n "$API_KEY" ]; then
    echo "🔑 Using provided API Key"
fi


if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    PYTHON_CMD="py"
else
    PYTHON_CMD="python3"
fi


PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)

VERSION_NUM=$(echo "$PYTHON_VERSION" | grep -oP '(?<=Python )\d+\.\d+')

MAJOR=$(echo  "$VERSION_NUM" | cut -d '.' -f 1)
MINOR=$(echo  "$VERSION_NUM" | cut -d '.' -f 2)

if [["$MAJOR" -lt 3]] || [["$MINOR" -eq 3]] && [["$MINOR" -lt 12]]; then
    echo "❌ Python 3.12 or higher is required. You have Python $VERSION_NUM"
    exit 1
else
    echo "✅ Python $VERSION_NUM is acceptable (>= 3.12)"
fi


function check_venv() {
    echo "💡 Activating virtual environment..."
    if [[ "$OSTYPE" == "darwin"* || "$OSTYPE" == "linux-gnu"* ]]; then
        source .venv/bin/activate
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        source .venv/Scripts/activate
    else
        echo "⚠️ Unsupported OS type: $OSTYPE"
        exit 1
    fi
}


if [ ! -d ".venv" ]; then
    echo "💡 Creating virtual environment..."
    $PYTHON_CMD -m venv .venv
    echo "📦 Installing dependencies..."
    check_venv
    pip install -r requirements.txt
else
    echo "✅ Virtual environment already exists."
    check_venv
fi


cd ./app || { echo "❌ 'app' directory not found!"; exit 1; }


if [ -n "$API_KEY" ]; then
    $PYTHON_CMD main.py --city="$CITY" --topic="$TOPIC" --key="$API_KEY"
else
    $PYTHON_CMD main.py --city="$CITY" --topic="$TOPIC"
fi

echo "✅ Done! Check the generated Excel file."
