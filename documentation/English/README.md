# English documentation

Open `main.tex` in TeXstudio, select **XeLaTeX** as the compiler, and build twice. `config.tex` contains fonts, colors, links, code-listing rules, and reusable boxes. The six files in `chapters/` hold the tutorial content and are included by `main.tex`; compile only `main.tex`.

The source prefers TeX Gyre Pagella and falls back to DejaVu Serif. It also locates `code/bot.py` whether compilation starts in this directory or at the repository root.

Generated PDFs and LaTeX helper files are intentionally ignored by Git. Share a built PDF through a GitHub Release if needed, while keeping the repository light.
