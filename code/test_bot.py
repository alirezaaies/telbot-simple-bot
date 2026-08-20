"""Small standard-library tests for the bot's deterministic reply text.

These tests do not contact Telegram and do not need a real bot token.
Run them after installing requirements.txt with: python -m unittest -v
"""

import unittest

from bot import echo_reply, help_reply, start_reply


class ReplyTests(unittest.TestCase):
    """Verify the exact messages readers should see in Telegram."""

    def test_start_reply_uses_the_given_name(self) -> None:
        self.assertTrue(start_reply("Alireza").startswith("Hello, Alireza!"))

    def test_start_reply_handles_a_missing_name(self) -> None:
        self.assertTrue(start_reply(None).startswith("Hello, there!"))

    def test_echo_reply_repeats_text(self) -> None:
        self.assertEqual(echo_reply("My first bot"), "You said: My first bot")

    def test_help_reply_contains_start_command(self) -> None:
        self.assertIn("/start", help_reply())


if __name__ == "__main__":
    unittest.main()
