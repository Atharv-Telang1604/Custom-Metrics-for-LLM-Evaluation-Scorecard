import os

# Load API key from environment for safety. Set the environment variable
# `OPENROUTER_API_KEY` before running the code.
API_KEY = os.environ.get("OPENROUTER_API_KEY")

# If you want a placeholder for local testing, set the variable in your shell:
# Windows PowerShell: $env:OPENROUTER_API_KEY = "your_api_key"
# Linux/macOS: export OPENROUTER_API_KEY="your_api_key"