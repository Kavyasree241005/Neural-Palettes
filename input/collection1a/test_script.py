import os
import json
import time
from pdf_structure_extractor import PDFStructureExtractor  # Make sure this file has the correct class

# Define the input and output directories
input_dir = "input"
output_dir = "output"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Create an instance of the PDFStructureExtractor
extractor = PDFStructureExtractor()

# Process each PDF in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".pdf"):
        filepath = os.path.join(input_dir, filename)
        print(f"Processing: {filepath}")

        start_time = time.time()
        result = extractor.process_pdf(filepath)
        end_time = time.time()

        # Define the output JSON filename
        output_filename = os.path.splitext(filename)[0] + "_output.json"
        output_path = os.path.join(output_dir, output_filename)

        # Write the result to the JSON file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"Saved to: {output_path}")
        print(f"Time taken: {end_time - start_time:.2f} seconds\n")