from __future__ import annotations

from pathlib import Path
from typing import List

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
MD_PATH = OUTPUT_DIR / "recommendation_report.md"
PDF_PATH = OUTPUT_DIR / "recommendation_report.pdf"

TITLE = "Programming Assignment 2"
SUBTITLE = "CoffeeTime Standortanalyse"
COURSE = "Kurs IMBIT23A"
AUTHORS = "Elyas Moukhli, Samuel Atama, Malik Yildizhan, Santiago Mehjide"


def is_table_separator(line: str) -> bool:
    return set(line.replace("|", "").strip()) <= {"-", ":"}


def parse_markdown_table(lines: List[str], page_width: float) -> Table:
    rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in lines
        if line.strip()
    ]
    data = [rows[0]] + rows[2:]

    styles = getSampleStyleSheet()
    cell_style = styles["BodyText"]
    header_style = styles["BodyText"]

    wrapped_data = [
        [Paragraph(cell, header_style) for cell in data[0]]
    ] + [[Paragraph(cell, cell_style) for cell in row] for row in data[1:]]

    col_count = max(len(row) for row in data)
    col_width = page_width / max(col_count, 1)
    col_widths = [col_width] * col_count

    table = Table(wrapped_data, colWidths=col_widths, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def build_story(page_width: float) -> list:
    styles = getSampleStyleSheet()
    story: list = []

    story.append(Paragraph(TITLE, styles["Title"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(SUBTITLE, styles["Heading2"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph(AUTHORS, styles["BodyText"]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(COURSE, styles["BodyText"]))
    story.append(PageBreak())

    content_lines = MD_PATH.read_text(encoding="utf-8").splitlines()
    idx = 0
    while idx < len(content_lines):
        line = content_lines[idx]
        if line.startswith("# "):
            story.append(Paragraph(line[2:].strip(), styles["Heading1"]))
            story.append(Spacer(1, 0.2 * cm))
            idx += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(line[3:].strip(), styles["Heading2"]))
            story.append(Spacer(1, 0.2 * cm))
            idx += 1
            continue
        if line.strip().startswith("|") and idx + 1 < len(content_lines):
            if is_table_separator(content_lines[idx + 1]):
                table_lines = [line, content_lines[idx + 1]]
                idx += 2
                while idx < len(content_lines) and content_lines[idx].strip().startswith("|"):
                    table_lines.append(content_lines[idx])
                    idx += 1
                story.append(parse_markdown_table(table_lines, page_width))
                story.append(Spacer(1, 0.3 * cm))
                continue
        if line.strip():
            story.append(Paragraph(line.strip(), styles["BodyText"]))
            story.append(Spacer(1, 0.15 * cm))
        else:
            story.append(Spacer(1, 0.25 * cm))
        idx += 1

    return story


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )
    page_width = doc.width
    story = build_story(page_width)
    doc.build(story)
    print(f"PDF erstellt: {PDF_PATH}")


if __name__ == "__main__":
    main()
