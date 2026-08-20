"""Run a small Telegram bot with the pyTelegramBotAPI (telebot) library.

The bot answers /start and /help, repeats normal text messages, and explains
what to do when it receives another content type. The Telegram token is read
from the BOT_TOKEN environment variable so that no secret is stored in code.

Author: Alireza Khajehvandi
Project: https://github.com/alirezaaies/telbot-simple-bot
"""

from __future__ import annotations

import os

import telebot
from telebot import types

# OPTIONAL .env MODE:
# Uncomment the next import and the matching load_dotenv() call in main() if
# you prefer to keep BOT_TOKEN in code/.env instead of exporting it manually.
# from dotenv import load_dotenv


def start_reply(first_name: str | None) -> str:
    """Return the welcome message used by the /start command."""
    name = first_name or "there"
    return (
        f"Hello, {name}!\n\n"
        "I am your first Telegram bot.\n"
        "Send me any text and I will repeat it.\n\n"
        "Commands:\n"
        "/start - show the welcome message\n"
        "/help - show usage help"
    )


def help_reply() -> str:
    """Return a short, beginner-friendly help message."""
    return (
        "How to use this bot:\n"
        "1. Send any text message.\n"
        "2. The bot replies with the same text.\n"
        "3. Send /start whenever you want to see the welcome message again."
    )


def echo_reply(text: str) -> str:
    """Build the reply for a normal text message."""
    return f"You said: {text}"


def create_bot(token: str) -> telebot.TeleBot:
    """Create the bot and register all message handlers."""
    if not token.strip():
        raise ValueError("The Telegram bot token cannot be empty.")

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def handle_start(message: types.Message) -> None:
        """Welcome the user and list the available commands."""
        bot.reply_to(message, start_reply(message.from_user.first_name))

    @bot.message_handler(commands=["help"])
    def handle_help(message: types.Message) -> None:
        """Explain how the bot behaves."""
        bot.reply_to(message, help_reply())

    @bot.message_handler(content_types=["text"])
    def handle_text(message: types.Message) -> None:
        """Repeat every ordinary text message."""
        bot.reply_to(message, echo_reply(message.text or ""))

    @bot.message_handler(
        content_types=["audio", "document", "photo", "sticker", "video", "voice"]
    )
    def handle_unsupported_content(message: types.Message) -> None:
        """Guide the user when this tutorial bot receives non-text content."""
        bot.reply_to(message, "Please send a text message so I can repeat it.")

    return bot


def main() -> None:
    """Read configuration and keep the bot connected to Telegram."""
    # OPTIONAL .env MODE: uncomment this together with the import near the top.
    # Existing terminal variables take priority because override is False.
    # load_dotenv(override=False)

    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit(
            "BOT_TOKEN is missing. Export it in your terminal or enable .env loading."
        )

    bot = create_bot(token)
    print("Bot is running. Press Ctrl+C to stop it.")
    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    main()
