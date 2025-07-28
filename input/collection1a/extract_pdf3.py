import fitz  # PyMuPDF
import os
import json

def is_bold(font_name):
    font_name = font_name.lower()
    return "bold" in font_name or "black" in font_name or "heavy" in font_name

def extract_bold_headings(pdf_path):
    doc = fitz.open(pdf_path)
    bold_headings = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for b in blocks:
            if "lines" not in b:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    if is_bold(s["font"]):
                        text = s["text"].strip()
                        if text and not text.isspace():
                            bold_headings.append({
                                "text": text,
                                "page": page_num
                            })

    return bold_headings

if __name__ == "__main__":
    pdf_file = "input/file03.pdf"
    output_file = "output/file03_bold_headings.json"

    if not os.path.exists("output"):
        os.makedirs("output")

    bold_data = extract_bold_headings(pdf_file)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(bold_data, f, indent=2, ensure_ascii=False)

    print(f" Extracted {len(bold_data)} bold headings from '{pdf_file}' → saved to '{output_file}'")
