# Learning Notes - Technical Concepts

This document explains the technical concepts used in the Email Segregation project in beginner-friendly terms.

## FastAPI

**What is it?**
FastAPI is a modern web framework for building APIs (backends). It makes it easy to create endpoints that handle HTTP requests.

**How it works in this project:**
1. When you submit the form on the website, it sends an HTTP POST request to `/extract`
2. FastAPI receives the request and passes the email text to our classifier and extractor
3. The classifier decides what category the email is, and the extractor pulls out the important fields
4. FastAPI sends back a JSON response with the results

**Key concepts:**
- **Endpoint**: A URL that does something (like `/extract`)
- **Request**: Data sent TO the server (the email text)
- **Response**: Data sent FROM the server (the results)
- **JSON**: A format for storing and sending data

## Regex (Regular Expressions)

**What is it?**
Regex is a powerful way to find and extract text patterns from strings.

**Simple examples:**
- `\bOPEN\b` - Find the word "OPEN" as a whole word (not part of another word)
- `\d+` - Find one or more digits (0-9)
- `[A-Z]+` - Find one or more capital letters
- `\s+` - Find one or more whitespace characters (spaces, tabs)

**In this project:**
We use regex to find keywords and extract specific fields:
```python
# Find vessel name after "MV" or "M/V"
VESSEL_NAME_PATTERN = r'(?i)\bM\/?V\.?\s+(?P<vessel>[A-Z0-9]+)'
```

Breaking it down:
- `(?i)` - Case insensitive (match both "MV" and "mv")
- `\b` - Word boundary (start of a word)
- `M\/?V\.?` - Match "MV", "M/V", "M.V", etc.
- `\s+` - One or more spaces
- `(?P<vessel>...)` - Capture the vessel name in a named group called "vessel"

## Rule-Based Classification

**What is it?**
Instead of using AI/ML, we use simple rules (if-then logic) to decide what category an email is.

**How it works:**
1. Define keywords for each category
2. Count how many keywords match in the email
3. The category with the most matches wins

**Example:**
```
Tonnage keywords: OPEN, MV, DWT, O/A, ONW, VSL
Cargo VC keywords: LOAD PORT, DISCHARGE PORT, POL, POD, LAYCAN
Cargo TC keywords: TCT, DELIVERY, REDELIVERY, DURATION, ACC

Email text: "MV SHENG AN HAI DWT 56564 OPEN XIAMEN O/A 2ND JUNE"

Tonnage matches: OPEN, MV, DWT, O/A = 4 matches
Cargo VC matches: 0 matches
Cargo TC matches: 0 matches

Result: Category = Tonnage (most matches)
Confidence = 4 / 6 keywords = 67%
```

**Why this approach?**
- Simple to understand and explain
- No need for external AI services
- Easy to tune (just add more keywords or patterns)
- Transparent (you can see why a decision was made)

## JSON (JavaScript Object Notation)

**What is it?**
JSON is a standard format for storing and sending data. It's easy for both humans and computers to read.

**Structure:**
```json
{
  "category": "tonnage",
  "confidence": 0.95,
  "data": {
    "vessel_name": "SHENG AN HAI",
    "vessel_size": "56564",
    "open_port": "XIAMEN, CHINA"
  }
}
```

**Key-value pairs:**
- `"category"` is the key, `"tonnage"` is the value
- The value can be a string, number, object, or array
- Objects use `{}` and arrays use `[]`

## Confidence Scoring

**How it works:**
```
confidence = (matching_keywords / total_keywords) + 0.1 bonus if >= 3 matches
capped at 1.0 (100%)

Example:
- Category has 6 keywords
- Email matches 4 keywords = 4/6 = 0.67
- 4 >= 3 so +0.1 bonus
- Final confidence = 0.77 = 77%
```

**Why this scoring?**
- More matching keywords = higher confidence
- Successfully extracted fields = validation
- Confidence helps users understand reliability

## Key Takeaways

1. **Simple is better** - This project uses straightforward logic
2. **Regex is powerful** - Pattern matching finds fields reliably
3. **Keyword matching works** - You don't need AI for categorization
4. **Confidence matters** - Users should know reliability
5. **Transparency** - Users can see what was found and why