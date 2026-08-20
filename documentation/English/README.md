# English documentation

Open `main.tex` in TeXstudio, select **XeLaTeX** as the compiler, and build twice. `config.tex` contains fonts, colors, links, code-listing rules, and reusable boxes. The six files in `chapters/` hold the tutorial content and are included by `main.tex`; compile only `main.tex`.

The source prefers TeX Gyre Pagella and falls back to DejaVu Serif. It also locates `code/bot.py` whether compilation starts in this directory or at the repository root.

The small final PDF is included for immediate reading. Temporary LaTeX helper
files remain ignored by Git. Every content page has a compact clickable social
footer; the cover provides the same destinations in its author block.
