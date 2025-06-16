#!/bin/bash
echo "📦 Installing dependencies..."
pip install pip-tools
./setup-dev-env.sh

echo "🚀 Starting Streamlit app..."
PYTHONPATH=. python -m streamlit run src/app.py