# Email Segregation MVP

A web-based system for automatic classification and data extraction from shipping emails.

## Features
- ✅ Classify emails into 3 categories (Tonnage, Cargo VC, Cargo TC)
- ✅ Extract key commercial fields using regex patterns
- ✅ No external LLM APIs required
- ✅ Built with FastAPI backend and HTML/CSS/JavaScript frontend
- ✅ Confidence scoring (0-100%)
- ✅ Clean JSON API

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Running
```bash
python main.py
```

Then open http://127.0.0.1:8000 in your browser.

## Categories

### Tonnage (Open Vessels)
Emails describing vessel availability.
Example: "MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026"

### Cargo VC (Voyage Charter)
Emails describing cargo for a specific voyage.
Example: "15,000 MTS CARGO LOAD PORT: THAILAND DISCHARGE PORT: KANDLA LAYCAN: MID JULY"

### Cargo TC (Time Charter)
Emails describing time charter requirements.
Example: "ACC COMPANY DELIVERY VANCOUVER REDELIVERY CHITTAGONG DURATION 30 DAYS"

## Architecture

- **Backend**: FastAPI with Python
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Classification**: Rule-based keyword matching
- **Extraction**: Regex patterns with named capture groups

## Documentation

- QUICKSTART.md - Installation and running instructions
- DOCUMENT_ANALYSIS.md - Business requirements and analysis
- REGEX_GUIDE.md - Detailed regex pattern explanations
- TEST_CASES.md - Sample emails and test cases
- LEARNING_NOTES.md - Technical concepts explained
- PROJECT_EXPLANATION.md - Complete data flow

## API

### POST /extract

Request:
```json
{
  "email_text": "raw email text here"
}
```

Response:
```json
{
  "category": "tonnage",
  "confidence": 0.95,
  "data": {
    "vessel_name": "SHENG AN HAI",
    "vessel_size": "56564",
    "open_port": "XIAMEN, CHINA",
    "open_date": "2ND JUNE 2026"
  }
}
```

## Testing

Run automated tests:
```bash
python test_api.py
```

Or manually test by pasting sample emails in the web interface.

## License

MIT