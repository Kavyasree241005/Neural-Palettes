# PDF Structure Extractor - Adobe India Hackathon 2025

## Overview
This solution extracts hierarchical document structure (title and headings H1, H2, H3) from PDF documents and outputs them in JSON format.

## Features
- Extracts document title and hierarchical headings (H1, H2, H3)
- Handles various PDF formats (application forms, posters, study materials, etc.)
- Uses multiple extraction methods for robustness (PyMuPDF + pdfplumber fallback)
- Font-size based heading classification with intelligent thresholds
- Outputs clean JSON format as specified
- Runs offline with no network dependencies
- Optimized for performance (≤10 seconds for 50-page PDFs)

## Architecture
The solution uses a multi-layered approach:

1. **Primary Extraction**: PyMuPDF for detailed font and formatting information
2. **Fallback Method**: pdfplumber for cases where PyMuPDF fails
3. **Smart Classification**: Dynamic font-size thresholds based on document characteristics
4. **Text Filtering**: Intelligent filtering to identify genuine headings vs. noise

## Docker Usage

### Build the image:
```bash
docker build --platform linux/amd64 -t pdf-extractor:v1 .
```

### Run the container:
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-extractor:v1
```

## Input/Output Format

### Input
- PDF files placed in `/app/input` directory
- Supports PDFs up to 50 pages
- Handles various PDF formats and layouts

### Output
JSON files in `/app/output` directory with format:
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## Algorithm Details

### Title Extraction
1. Analyzes first 2 pages of document
2. Identifies largest font size text
3. Filters out page numbers, metadata, and noise
4. Selects most appropriate title candidate

### Heading Classification
1. Extracts all text with font formatting information
2. Calculates dynamic font-size thresholds based on document
3. Classifies headings using both relative and absolute font sizes
4. Filters text using heading-specific patterns and characteristics

### Performance Optimizations
- Efficient text extraction with minimal memory usage
- Smart filtering to reduce processing overhead
- Optimized font analysis algorithms
- Limited output to prevent excessive processing

## Dependencies
- PyMuPDF (1.23.26): Primary PDF processing
- pdfplumber (0.10.3): Fallback PDF processing
- Standard Python libraries for JSON and text processing

## Constraints Met
- ✅ Execution time: ≤10 seconds for 50-page PDF
- ✅ No network access required
- ✅ Model size: <200MB (no ML models used)
- ✅ CPU-only operation (AMD64 compatible)
- ✅ Memory efficient for 16GB RAM systems

## Testing
Run the test script to validate functionality:
```bash
python test_script.py
```

## Error Handling
- Graceful fallback between extraction methods
- Comprehensive error logging
- Safe output generation even on processing failures
- Handles corrupted or unusual PDF formats