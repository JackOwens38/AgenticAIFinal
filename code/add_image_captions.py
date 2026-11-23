#!/usr/bin/env python3
"""
add_image_captions.py  —  Fill the "Visual Description (colours & appearance)" column
of the Artworks sheet by showing each artwork's image to a vision model.

WHY: the RAG chatbot is text-only; it cannot look at a JPEG. This script does the
"looking" once, at data-prep time, and writes a short factual description (dominant
colours, what is depicted, composition) into the spreadsheet. After you run it, those
descriptions get embedded like any other column, so questions such as
"what colours are used in Spring?" can be answered.

RUN IT where the museum image URLs are reachable (e.g. Google Colab) — NOT inside the
chatbot. It edits the .xlsx in place (all other sheets are preserved).

SETUP (Colab):
    !pip install openpyxl openai
    import os; os.environ["OPENAI_API_KEY"] = "sk-..."   # your key
    # upload Raclin_Murphy_Museum_Galleries_Dataset.xlsx, then:
    !python add_image_captions.py Raclin_Murphy_Museum_Galleries_Dataset.xlsx

Options:  --limit N  (caption only the first N empty rows, for a cheap test)
          --overwrite  (re-caption rows that already have a description)
"""
import sys, os, time, argparse
from openpyxl import load_workbook

HEADER_ROW = 4          # matches the workbook layout (two banner rows, header on row 4)
IMG_COL_NAME  = "Primary Image (JPEG URL)"
DESC_COL_NAME = "Visual Description (colours & appearance)"
TITLE_COL_NAME = "Title"
MODEL = "gpt-4o-mini"   # cheap vision model; any vision model works

PROMPT = ("You are cataloguing a museum artwork. Look at the image and write 1-2 plain "
          "factual sentences a visitor could use: name the DOMINANT COLOURS, what is "
          "depicted (subject/forms), and the overall composition or style. No preamble, "
          "no interpretation of meaning, under 45 words. If the image is missing or not "
          "an artwork, reply exactly: (no image).")

def caption(client, url, title):
    r = client.chat.completions.create(
        model=MODEL, max_tokens=90, temperature=0,
        messages=[{"role":"user","content":[
            {"type":"text","text":f"Artwork title: {title}\n{PROMPT}"},
            {"type":"image_url","image_url":{"url":url}},
        ]}])
    return r.choices[0].message.content.strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--sheet", default="Artworks")
    a = ap.parse_args()

    from openai import OpenAI
    client = OpenAI()

    wb = load_workbook(a.xlsx)
    ws = wb[a.sheet]
    hdr = {ws.cell(HEADER_ROW, c).value: c for c in range(1, ws.max_column+1)}
    for need in (IMG_COL_NAME, DESC_COL_NAME, TITLE_COL_NAME):
        if need not in hdr:
            sys.exit(f"Column '{need}' not found on sheet '{a.sheet}'. Headers: {list(hdr)}")
    ic, dc, tc = hdr[IMG_COL_NAME], hdr[DESC_COL_NAME], hdr[TITLE_COL_NAME]

    done = 0
    for row in range(HEADER_ROW+1, ws.max_row+1):
        url = ws.cell(row, ic).value
        if not url or not str(url).startswith("http"):
            continue
        if ws.cell(row, dc).value and not a.overwrite:
            continue
        title = ws.cell(row, tc).value or ""
        try:
            desc = caption(client, str(url), str(title))
        except Exception as e:
            print(f"  row {row} ERROR: {e}"); time.sleep(2); continue
        if desc and desc != "(no image)":
            ws.cell(row, dc).value = desc
            print(f"  [{title}] -> {desc}")
            done += 1
        if a.limit and done >= a.limit:
            break
        time.sleep(0.4)   # be polite to the image host / API

    wb.save(a.xlsx)
    print(f"\nDone. Captioned {done} rows. Saved {a.xlsx}. Re-run your notebook's build cell to re-embed.")

if __name__ == "__main__":
    main()
