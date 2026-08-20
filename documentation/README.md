# Documentation build guide

The English and Persian editions have the same six chapters, complete code, commands, checkpoints, expected output, troubleshooting, and next steps. Only the language and writing direction differ.

## Requirements

Install a TeX distribution that includes XeLaTeX and these commonly available packages:

```text
fontspec, geometry, xcolor, graphicx, fontawesome5, eso-pic,
booktabs, enumitem, listings, tcolorbox, fancyhdr, titlesec,
hyperref, xepersian
```

TeX Live users may need the `texlive-xetex`, `texlive-latex-extra`, and Persian/language collections supplied by their operating system. MiKTeX can install missing packages when prompted. Package names differ between operating systems, so use your distribution's package manager.

## Build in TeXstudio

1. Open `English/main.tex` or `Persian/main.tex`.
2. In TeXstudio, select **Options → Configure TeXstudio → Build**.
3. Set the default compiler to **XeLaTeX**.
4. Build `main.tex` twice to refresh the table of contents.

Do not compile `config.tex` or a chapter by itself. Both entry files contain TeXstudio magic comments that select XeLaTeX and UTF-8.

The English configuration prefers **TeX Gyre Pagella** and falls back to **DejaVu Serif**. The Persian configuration uses XePersian, prefers **IRANSansX**, and falls back to **B Nazanin** and then **Noto Naskh Arabic**. Change only the font selection lines in `config.tex` if none of those fonts is installed.

## Source structure

Each edition contains:

- `main.tex`: cover, contents, chapter order, author links;
- `config.tex`: packages, fonts, colors, headers, listings, reusable boxes;
- `chapters/*.tex`: one topic per editable chapter;
- `README.md`: edition-specific notes.

Chapter 4 imports the real `code/bot.py`, so the printed complete code cannot silently drift away from the implementation. Compile from the edition folder or repository root; the configuration supports both locations.

## Generated files

The two small final PDFs are included in this repository for immediate reading.
Temporary LaTeX products remain ignored to avoid noisy commits. If a build
behaves strangely, delete its generated helper files locally and compile
`main.tex` twice again.
