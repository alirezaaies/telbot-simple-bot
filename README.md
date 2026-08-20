# Build Your First Telegram Bot with TeleBot

A small, practical, bilingual tutorial that takes a complete beginner from an empty setup to a working Telegram echo bot. The same hands-on book is available as editable English and Persian LaTeX source.

Created by **[Alireza Khajehvandi](https://alirezaaies.github.io/)**.

## What you will build

The bot uses Python and the `telebot` module from `pyTelegramBotAPI`. It:

- welcomes users with `/start`;
- explains usage with `/help`;
- repeats ordinary text as `You said: ...`;
- guides users who send a photo, voice note, or other supported non-text content.

No database, web server, or paid service is needed for this local tutorial.

## Start in five minutes

You need Python 3.10 or newer, a Telegram account, and an internet connection.

```bash
git clone https://github.com/alirezaaies/telbot-simple-bot.git
cd telbot-simple-bot/code
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, create and activate the environment with:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

In Telegram, open the verified `@BotFather`, send `/newbot`, follow its prompts, and keep the resulting token private. Set it in the same terminal where you will run the bot:

```bash
export BOT_TOKEN="paste_your_token_here"       # macOS/Linux
python bot.py
```

```powershell
$env:BOT_TOKEN="paste_your_token_here"         # Windows PowerShell
python bot.py
```

Open your new bot in Telegram, press **Start**, then send `My first bot`. The exact reply is:

```text
You said: My first bot
```

Stop the program with `Ctrl+C`. Run its offline checks with `python -m unittest -v` from the `code` folder.

> Never commit or share a real token. If it is exposed, use `/revoke` in BotFather immediately and create a replacement. `.env` is ignored by Git, and `.env.example` contains only a safe placeholder.

## Repository map

```text
telbot-simple-bot/
├── code/
│   ├── bot.py                 # complete, commented bot
│   ├── requirements.txt       # one pinned runtime dependency
│   ├── test_bot.py            # four offline reply tests
│   └── README.md              # code-specific guide
├── documentation/
│   ├── English/               # English XeLaTeX book
│   ├── Persian/               # Persian XePersian book (RTL)
│   └── README.md              # documentation build guide
├── LINKEDIN_POST.md           # ready-to-publish launch caption
├── LICENSE
└── README.md
```

## Compile the tutorial books

The documentation is written as a styled, chapter-based practical book. Open either edition's `main.tex` in TeXstudio, select **XeLaTeX**, and compile twice so the table of contents is current:

- English: [`documentation/English/main.tex`](documentation/English/main.tex)
- Persian: [`documentation/Persian/main.tex`](documentation/Persian/main.tex)

Compile `main.tex`, not an individual chapter. The Persian edition uses XePersian and prefers `IRANSansX`; it automatically falls back to `B Nazanin`, then `Noto Naskh Arabic`. See the [documentation build guide](documentation/README.md) for the expected TeX packages and troubleshooting.

PDF, AUX, LOG, TOC, SyncTeX, and other generated files are ignored to keep the Git history small. Build them locally. If readers need a ready-made PDF, attach it to a GitHub Release instead of committing repeated build output.

## فارسی — شروع سریع

این مخزن یک آموزش عملی یکسان به دو زبان فارسی و انگلیسی است. ربات با پایتون و کتابخانهٔ `telebot` ساخته می‌شود، به دستورهای `/start` و `/help` پاسخ می‌دهد و متن کاربر را تکرار می‌کند.

برای شروع، وارد پوشهٔ `code` شوید، یک محیط مجازی بسازید، دستور `python -m pip install -r requirements.txt` را اجرا کنید و توکن دریافتی از `@BotFather` را در متغیر `BOT_TOKEN` قرار دهید. سپس با دستور `python bot.py` ربات را روشن کنید. توکن واقعی را هرگز در کد یا گیت ننویسید.

برای مطالعه و ساخت کتاب فارسی، فایل [`documentation/Persian/main.tex`](documentation/Persian/main.tex) را در TeXstudio باز کنید، موتور XeLaTeX را انتخاب کنید و دو بار خروجی بگیرید. کدها در هر دو نسخه دقیقاً یکسان هستند.

## Questions and contributions

If a step is unclear or behaves differently on your system, open a GitHub issue with your operating system, Python version, command, and complete error message—remove tokens and private information first. Focused pull requests that keep both language editions synchronized are welcome.

If this project helped you, star the repository and share what you built.

## Connect with Alireza Khajehvandi

- [LinkedIn](https://www.linkedin.com/in/alirezakhajehvandi)
- [YouTube](https://www.youtube.com/@AlirezaAIES)
- [Telegram channel](https://t.me/AlirezaAIES)
- [Instagram](https://www.instagram.com/alireza.aies)
- [GitHub](https://github.com/alirezaaies)
- [Personal website and portfolio](https://alirezaaies.github.io/)

## License

This project is available under the [MIT License](LICENSE).
