# menuBot

Simple Telegram bot skeleton for a restaurant menu.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install python-telegram-bot~=20.0 python-dotenv
   ```

2. Create a `.env` file by copying `.env.example` and set your `TELEGRAM_BOT_TOKEN`:
   ```bash
   cp .env.example .env
   # Edit .env and set TELEGRAM_BOT_TOKEN=your_token
   ```

3. Run the bot:
   ```bash
   python bot.py
   ```
