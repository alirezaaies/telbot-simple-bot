# Bot code

This folder contains everything needed to run the tutorial bot. The bot uses Python and the `telebot` module supplied by `pyTelegramBotAPI`.

## What each file does

| File | Purpose |
|---|---|
| `bot.py` | The complete bot: `/start`, `/help`, text echo, and non-text guidance |
| `requirements.txt` | TeleBot plus the optional `.env` loader, pinned for repeatable installation |
| `.env.example` | A safe template for readers who choose the optional `.env` method |
| `test_bot.py` | Offline tests for the exact reply text |

## Quick start

Use Python 3.10 or newer. From this directory:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Ask Telegram's verified `@BotFather` for a bot token and keep it private. Choose
one of the following methods.

### Method A — terminal variable (default)

Set the token only in the current terminal:

```bash
export BOT_TOKEN="paste_your_token_here"       # macOS/Linux
```

```powershell
$env:BOT_TOKEN="paste_your_token_here"         # Windows PowerShell
```

This value disappears when the terminal closes. Set it again in every new
terminal session.

### Method B — local `.env` file (optional)

Create your private file from the safe template:

```bash
cp .env.example .env                            # macOS/Linux
```

```powershell
Copy-Item .env.example .env                     # Windows PowerShell
```

Open `.env`, replace the placeholder after `BOT_TOKEN=`, and save it. Then
uncomment these two marked lines in `bot.py`:

```python
from dotenv import load_dotenv
```

```python
load_dotenv(override=False)
```

The import is near the top of the file and the function call is at the beginning
of `main()`. The `python-dotenv` package is already included in
`requirements.txt`. With `override=False`, a token exported in the terminal wins
if both methods are present.

Run and test:

```bash
python bot.py
```

Open your bot in Telegram, press **Start**, and send `My first bot`. It replies with `You said: My first bot`. Stop it with `Ctrl+C`.

Run the offline checks with:

```bash
python -m unittest -v
```

Never paste a real token into `bot.py`, `.env.example`, a screenshot, a commit,
or a message. Only the ignored `.env` file may contain it. Before committing,
confirm that `git status` does not list `code/.env`. If a token leaks, use
`/revoke` in BotFather immediately and create a replacement.

Author: [Alireza Khajehvandi](https://alirezaaies.github.io/)
