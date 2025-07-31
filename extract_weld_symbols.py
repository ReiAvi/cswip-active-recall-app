import fitz  # PyMuPDF
import os

# Path to your PDF and output directory
pdf_path = "data/WeldSymbol_UNE-EN_ISO_2553=2020(EN).pdf"
output_dir = "weld_symbols/elementary/"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Open the PDF document
doc = fitz.open(pdf_path)

# List of symbols to extract with their respective page numbers
# Adjust page numbers as needed (1-based in your reference, 0-based in PyMuPDF)
symbols_to_extract = {
    "E10_fillet": {"page": 5},
    "E01_square_butt": {"page": 5}
    # Add more as needed, e.g. "E02_single_v_butt": {"page": 6}
}

for symbol_id, data in symbols_to_extract.items():
    page = doc[data["page"] - 1]  # Convert to 0-based index
    svg_data = page.get_svg_image(matrix=fitz.Matrix(1, 1))  # Full page as SVG

    svg_path = os.path.join(output_dir, f"{symbol_id}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_data)
    print(f"Saved {svg_path} (full page, crop manually in Inkscape)")

doc.close()
