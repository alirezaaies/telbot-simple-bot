# Bot code

This folder contains everything needed to run the tutorial bot. The bot uses Python and the `telebot` module supplied by `pyTelegramBotAPI`.

## What each file does

| File | Purpose |
|---|---|
| `bot.py` | The complete bot: `/start`, `/help`, text echo, and non-text guidance |
| `requirements.txt` | The single required third-party package, pinned for repeatable installation |
| `.env.example` | A safe token placeholder; it does not contain a real secret |
| `test_bot.py` | Offline tests for the exact reply text |

## Quick start

Use Python 3.10 or newer. From this directory:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Ask Telegram's verified `@BotFather` for a bot token. Keep it private, then set it only in the current terminal:

```bash
export BOT_TOKEN="paste_your_token_here"       # macOS/Linux
```

```powershell
$env:BOT_TOKEN="paste_your_token_here"         # Windows PowerShell
```

Run and test:

```bash
python bot.py
```

Open your bot in Telegram, press **Start**, and send `My first bot`. It replies with `You said: My first bot`. Stop it with `Ctrl+C`.

Run the offline checks with:

```bash
python -m unittest -v
```

Never paste a real token into `bot.py`, `.env.example`, a screenshot, a commit, or a message. If one leaks, use `/revoke` in BotFather immediately and create a replacement.

Author: [Alireza Khajehvandi](https://alirezaaies.github.io/)
