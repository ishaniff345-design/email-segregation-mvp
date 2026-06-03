# Project Explanation - How Everything Works Together

This document explains the complete data flow and how each component works together.

## System Architecture

```
FRONTEND LAYER          API LAYER              PROCESSING LAYER
┌──────────────┐      ┌─────────────┐        ┌──────────────────┐
│  HTML Form   │      │ FastAPI     │        │ Classifier       │
│  with Textarea│─────▶│ /extract    │───────▶│ - Keyword count  │
│  and Buttons │      │ endpoint    │        │ - Scoring        │
└──────────────┘      └─────────────┘        └──────────────────┘
                           │
                           │ JSON Response
                           │
┌──────────────┐            │                ┌──────────────────┐
│  Display     │────────────┘                │ Extractor        │
│  Results     │                             │ - Regex patterns │
│  - Category  │                             │ - Field capture  │
│  - Confidence│                             │ - Data cleanup   │
│  - Fields    │                             └──────────────────┘
│  - JSON      │
└──────────────┘
```

## Data Flow

### 1. User Submits Email
User pastes email text and clicks "Extract & Classify"

### 2. Frontend Sends Request
JavaScript sends HTTP POST request with email_text as JSON

### 3. Backend Receives Request
FastAPI receives POST request to `/extract` endpoint

### 4. Classification Process
1. Count keywords for each category
2. Find category with highest count
3. Calculate confidence score

### 5. Field Extraction
1. Apply regex patterns for the category
2. Extract matching fields
3. Clean up values

### 6. Build Response
Wrap results in JSON response object

### 7. Frontend Displays Results
- Category badge (color-coded)
- Confidence percentage (0-100%)
- Extracted fields (in grid format)
- Raw JSON (for inspection)

## Classification Example

```
Input: "MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026"

Keyword Counting:
- OPEN found ✓
- MV found ✓
- DWT found ✓
- O/A found ✓

Tonnage matches: 4 out of 6 keywords
Cargo VC matches: 0 matches
Cargo TC matches: 0 matches

Result: Category = "tonnage"
Confidence = 4/6 + 0.1 bonus = 0.77 (77%)

Extraction:
- vessel_name: "SHENG AN HAI" (from MV pattern)
- vessel_size: "56564" (from DWT pattern)
- open_port: "XIAMEN, CHINA" (from OPEN pattern)
- open_date: "2ND JUNE 2026" (from O/A pattern)
```

## Response Format

```json
{
  "category": "tonnage",
  "confidence": 0.77,
  "data": {
    "vessel_name": "SHENG AN HAI",
    "vessel_size": "56564",
    "open_port": "XIAMEN, CHINA",
    "open_date": "2ND JUNE 2026"
  }
}
```

## Why This Approach Works

✅ **No external APIs** - All processing happens locally
✅ **Fast** - Results return instantly
✅ **Transparent** - You can see why a decision was made
✅ **Beginner-friendly** - Code is readable and explainable
✅ **Scalable** - Can handle many requests
✅ **Customizable** - Easy to add keywords or patterns