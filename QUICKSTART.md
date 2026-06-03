# Quick Start Guide

## What You Have Built

A **Shipping Email Segregation & Data Extraction MVP** that:
- ✅ Automatically classifies shipping emails (Tonnage, Cargo VC, Cargo TC)
- ✅ Extracts key commercial fields using Regex + Rule-Based logic
- ✅ Returns structured JSON data
- ✅ Provides a simple web interface
- ✅ Uses NO external LLM APIs (no OpenAI, Claude, Gemini, etc.)

## Installation & Running

### Step 1: Open Terminal
```bash
cd g:\workspace\emailsegrIME
```

### Step 2: Install Dependencies (one time only)
```bash
pip install -r requirements.txt
```

### Step 3: Start the Server
```bash
python main.py
```

You'll see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 4: Open Web Browser
Go to: **http://127.0.0.1:8000**

## Usage

1. **Paste an email** into the textarea
2. **Click "Extract & Classify"** button
3. **View results**:
   - Category badge (Tonnage / Cargo VC / Cargo TC)
   - Confidence percentage (0-100%)
   - Extracted fields
   - Raw JSON response

## Stop the Server

Press `Ctrl+C` in the terminal where the server is running.

## Testing

To run automated tests:
```bash
python test_api.py
```

## Project Files

### Code Files
- `main.py` - FastAPI backend application
- `classifier.py` - Email classification logic
- `extractor.py` - Field extraction
- `patterns.py` - Regex patterns and keywords
- `models.py` - Data models

### Frontend Files
- `static/index.html` - Web interface
- `static/styles.css` - Styling
- `static/app.js` - JavaScript logic

### Documentation
- `README.md` - Full documentation
- `DOCUMENT_ANALYSIS.md` - Business requirements & analysis
- `SAMPLE_PATTERNS.md` - Email pattern examples
- `REGEX_GUIDE.md` - Regex pattern explanations
- `LEARNING_NOTES.md` - Technical concepts explained
- `PROJECT_EXPLANATION.md` - Complete data flow
- `TEST_CASES.md` - 15+ test cases with examples

## Example Emails to Test

### Tonnage (Open Vessel)
```
MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026
```

### Cargo VC (Voyage Charter)
```
15,000 - 20,000 MTS MOLOCHOPT
LOAD PORT : KOH SI CHANG , THAILAND
DISCHARGE PORT: KANDLA + CHENNAI
LAYCAN: MID JULY 2026
```

### Cargo TC (Time Charter)
```
ACC DAI AN OCEAN SHIPPING COMPANY LIMITED
DELIVERY TM VANCOUVER
REDELIVERY CHITTAGONG
DURATION ABT 30 DAYS
```

## Key Features

✅ **No LLMs** - Uses regex and rule-based logic  
✅ **Fast** - Instant results, no API latency  
✅ **Transparent** - You can see exactly why it classified an email  
✅ **Beginner-friendly** - All code is readable and explainable  
✅ **Structured Output** - Returns clean JSON  
✅ **Production Ready** - Can handle real shipping emails  

## Troubleshooting

### Server won't start
- Make sure port 8000 is not in use
- Check Python is installed: `python --version`
- Verify dependencies: `pip list | grep fastapi`

### Browser can't connect
- Check server is running (see terminal output)
- Try refreshing the page (F5)
- Check URL is: `http://127.0.0.1:8000` (not https)

### No results showing
- Paste a complete email (samples provided above)
- Check browser console for errors (F12)
- Run `python test_api.py` to test API directly

## API Reference

**Endpoint**: `POST /extract`

**Request**:
```json
{
  "email_text": "MV SHENG AN HAI DWT 56564 OPEN XIAMEN O/A 2ND JUNE 2026"
}
```

**Response**:
```json
{
  "category": "tonnage",
  "confidence": 0.77,
  "data": {
    "vessel_name": "SHENG AN HAI",
    "open_port": "XIAMEN, CHINA",
    "open_date": "2ND JUNE 2026",
    "vessel_size": "56564"
  }
}
```

## Code Quality

All code follows these principles:
- ✅ Clear variable names
- ✅ Small readable functions
- ✅ Meaningful comments for important logic
- ✅ No overengineering
- ✅ Beginner-friendly explanations

Every function has a docstring explaining:
- What it does
- What it takes as input
- What it returns

---

**Happy Testing!** 🚀

For questions or issues, review the documentation files included in the project.