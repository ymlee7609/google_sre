# Google SRE 3-Book Knowledge Base

A comprehensive knowledge base built from Google's three public SRE books, converted to Markdown with study materials, cross-reference guides, and PPTX slide decks.

**[한국어 README](README_ko.md)**

## Books Included

| Book | Path | Files | Source |
|------|------|-------|--------|
| Site Reliability Engineering | `docs/sre-book/` | 44 | [sre.google/sre-book](https://sre.google/sre-book/table-of-contents/) |
| The Site Reliability Workbook | `docs/workbook/` | 29 | [sre.google/workbook](https://sre.google/workbook/table-of-contents/) |
| Building Secure & Reliable Systems | `docs/bsrs/` | 27 | [sre.google/books](https://sre.google/books/) |

**100 Markdown files** total (76 chapters + appendices + conclusions + summaries)

## Project Structure

```
google_sre/
├── docs/
│   ├── sre-book/           # SRE Book (Ch01-34, Appendix A-F, summaries)
│   │   └── summaries/      # Korean summaries per chapter (40 files)
│   ├── workbook/           # Workbook (Ch01-21, Appendix A-C, conclusion)
│   └── bsrs/               # BSRS (Ch01-21, Appendix A, conclusion)
├── scripts/
│   ├── download_sre_books.py       # Download & convert to Markdown
│   ├── build_pdf.py                # Markdown → PDF/HTML converter
│   ├── build_pptx.py               # SRE Book → PPTX (Nordic Minimalism)
│   ├── build_study_guide_pptx.py   # Study Guide → PPTX (Glassmorphism)
│   └── pdf_style.css               # PDF styling
└── output/
    ├── SRE_Study_Guide.md                  # 12-week cross-study guide
    ├── SRE_Study_Guide_Glassmorphism.pptx  # Study guide slides (26 slides)
    ├── SRE_Study_Part1-5_*.pptx            # SRE Book slides (5 volumes, 195 slides)
    ├── sre-book.pdf / .html                # SRE Book full export
    ├── workbook.pdf / .html                # Workbook full export
    └── bsrs.pdf / .html                    # BSRS full export
```

## Quick Start

### Prerequisites

```bash
pip install requests beautifulsoup4 python-pptx lxml
```

### Download Books

```bash
# Download all 3 books
python3 scripts/download_sre_books.py --book all

# Download a specific book
python3 scripts/download_sre_books.py --book sre-book

# Resume interrupted download
python3 scripts/download_sre_books.py --book workbook --resume

# Verify downloaded files
python3 scripts/download_sre_books.py --verify
```

### Generate Study Materials

```bash
# Build SRE Book PPTX slides (Nordic Minimalism, 5 volumes)
python3 scripts/build_pptx.py

# Build Cross-Study Guide PPTX (Glassmorphism, 26 slides)
python3 scripts/build_study_guide_pptx.py

# Build PDF/HTML exports
python3 scripts/build_pdf.py
```

## Study Materials

### 12-Week Cross-Study Curriculum

The [`output/SRE_Study_Guide.md`](output/SRE_Study_Guide.md) provides a structured 12-week learning plan that cross-references all three books:

| Week | Focus | Chapters |
|------|-------|----------|
| 1 | Part I: Introduction | 2 |
| 2-3 | Part II: Principles | 7 |
| 4-8 | Part III: Practices | 18 |
| 9-10 | Part IV: Management | 5 |
| 11 | Part V: Conclusions & Appendices | 2 + Appendices |
| 12 | Supplementary (unique chapters) | 9 |

### PPTX Slide Decks

| File | Design | Slides | Content |
|------|--------|--------|---------|
| `SRE_Study_Part1-5_*.pptx` | Nordic Minimalism | 195 | SRE Book chapter summaries |
| `SRE_Study_Guide_Glassmorphism.pptx` | Glassmorphism | 26 | Cross-study guide & references |

### Topic Quick Reference

| Topic | SRE Book | Workbook | BSRS |
|-------|----------|----------|------|
| SLO/SLI/SLA | Ch03-04 | Ch02-03, Ch05 | — |
| Monitoring/Alerting | Ch06, Ch10 | Ch04-05 | Ch15 |
| Incident Management | Ch13-14 | Ch09 | Ch17-18 |
| Postmortem | Ch15 | Ch10 | Ch18 |
| Toil/Automation | Ch05, Ch07 | Ch06 | — |
| On-Call | Ch11, Ch28 | Ch08 | — |
| Load Balancing/Overload | Ch19-22 | Ch11, Ch17 | Ch10 |
| Release/Deploy | Ch08 | Ch16 | Ch14 |
| Security | — | — | Ch01-21 |

## Claude Code Integration

Query SRE knowledge using the `/sre-knowledge` skill:

```
/sre-knowledge How should I set SLOs?
/sre-knowledge Best practices for postmortem writing
/sre-knowledge On-call rotation best practices
```

Responses always include source references (e.g., `[SRE Book Ch04]`, `[Workbook Ch02]`).

## License

Original content copyright belongs to Google, published under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/).
