"""
Regex patterns for email classification and field extraction.
Based on patterns found in the shipping email document.
"""

import re
from typing import Dict, List, Pattern

# Tonnage classification keywords
TONNAGE_KEYWORDS = [
    r'\bOPEN\b',
    r'\b(?:MV|M/V)\b',
    r'\bDWT\b',
    r'\bO/A\b',
    r'\bONW\b',
    r'\bVSL\s+PARTICULAR\b',
]

# Cargo VC classification keywords
CARGO_VC_KEYWORDS = [
    r'\bLOAD\s+PORT\b',
    r'\bDISCHARGE\s+PORT\b',
    r'\bPOL\b',
    r'\bPOD\b',
    r'\bLP\b',
    r'\bDP\b',
    r'\bLAYCAN\b',
    r'\bMTS?\b',
]

# Cargo TC classification keywords
CARGO_TC_KEYWORDS = [
    r'\bTCT\b',
    r'\bDELIVERY\b',
    r'\bREDELIVERY\b',
    r'\bDURATION\b',
    r'\bACC\b',
    r'\bA/C\b',
]

# Extraction patterns - Tonnage
VESSEL_NAME_PATTERN = r'(?i)\bM\/?V\.?\s+(?P<vessel>[A-Z0-9][A-Z0-9\s.\'-/]+?)(?:\s+DWT|\s+\d+|\s+OPEN|$)'
DWT_PATTERN = r'(?i)\bDWT\s*[:\-]?\s*(?P<size>[0-9][0-9,\.]*?)\b'
DWT_K_PATTERN = r'(?i)\b(?P<size>\d+(?:\.\d+)?)\s*K\s*DWT\b'
OPEN_PORT_PATTERN = r'(?i)\bOPEN\s+(?P<open_port>[A-Z][A-Z\s,.\'-/]+?)(?:\s+O/A|\s+\d{1,2}|\s+ONW|$)'
OPEN_DATE_OA_PATTERN = r'(?i)\bO/A\s*(?P<open_date>\d{1,2}(?:ST|ND|RD|TH)?\s+[A-Z]{3,9}(?:\s+\d{4})?)\b'
OPEN_DATE_ONW_PATTERN = r'(?i)\b(?P<open_date>\d{1,2}(?:ST|ND|RD|TH)?\s+[A-Z]{3,9})\s+ONW\b'

# Extraction patterns - Cargo VC
LOAD_PORT_PATTERN = r'(?i)\b(?:LOAD\s+PORT|POL|LP)\s*[:\-]?\s*(?P<loading_port>[A-Z][A-Z\s/+.\'-]+?)(?:\s+DISCHARGE|\s+POD|\s+DP|$)'
DISCHARGE_PORT_PATTERN = r'(?i)\b(?:DISCHARGE\s+PORT|POD|DP)\s*[:\-]?\s*(?P<discharge_port>[A-Z][A-Z\s/+.\'-]+?)(?:\s+LAYCAN|\s+LC|$)'
CARGO_QTY_NAME_PATTERN = r'(?i)\b(?P<quantity>\d[\d,.\s-]*?)\s*MTS?\s+(?P<cargo>[A-Z0-9][A-Z0-9\s\-/.,]+?)(?:\s+LOAD|\s+LP|\s+DISCHARGE|$)'
CARGO_LINE_PATTERN = r'(?i)\bCargo\s*[:\-]?\s*(?P<cargo_line>.+?)(?:\s+POL|\s+POD|$)'

# Extraction patterns - Cargo TC
DELIVERY_PATTERN = r'(?i)\b(?:DELIVERY|DELY)\s*(?:TM|TO)?\s*(?P<delivery_port>[A-Z][A-Z\s/+.\'-]+?)(?:\s+REDELIVERY|\s+LC|\s+LAYCAN|$)'
REDELIVERY_PATTERN = r'(?i)\b(?:REDELIVERY|REDEL)\s*(?P<redelivery_port>[A-Z][A-Z\s/+.\'-]+?)(?:\s+DURATION|\s+LC|\s+LAYCAN|$)'
DURATION_PATTERN = r'(?i)\bDURATION\s*[:\-]?\s*(?P<duration>(?:ABT\s*)?\d+\s*(?:-\s*\d+)?\s*DAYS?)\b'

# Common patterns
ACCOUNT_PATTERN = r'(?i)\b(?:ACC|A/C)\s+(?P<account>[A-Z0-9][A-Z0-9\s&.\'-/]+?)(?:\s+DELIVERY|\s+DELY|$)'
LAYCAN_PATTERN = r'(?i)\b(?:LAYCAN|LC)\s*[:\-]?\s*(?P<laycan>[A-Z0-9 ,\-/]+?)(?:\s+COM|\s+ADDCOM|\s+$)'
DATE_RANGE_PATTERN = r'(?i)\b(?P<date_range>\d{1,2}\s*-\s*\d{1,2}\s+[A-Z]{3,9}(?:\s+\d{4})?)\b'


def compile_patterns() -> Dict[str, Pattern]:
    """Compile all regex patterns."""
    patterns = {
        # Tonnage
        'vessel_name': re.compile(VESSEL_NAME_PATTERN),
        'dwt': re.compile(DWT_PATTERN),
        'dwt_k': re.compile(DWT_K_PATTERN),
        'open_port': re.compile(OPEN_PORT_PATTERN),
        'open_date_oa': re.compile(OPEN_DATE_OA_PATTERN),
        'open_date_onw': re.compile(OPEN_DATE_ONW_PATTERN),
        
        # Cargo VC
        'load_port': re.compile(LOAD_PORT_PATTERN),
        'discharge_port': re.compile(DISCHARGE_PORT_PATTERN),
        'cargo_qty_name': re.compile(CARGO_QTY_NAME_PATTERN),
        'cargo_line': re.compile(CARGO_LINE_PATTERN),
        
        # Cargo TC
        'delivery': re.compile(DELIVERY_PATTERN),
        'redelivery': re.compile(REDELIVERY_PATTERN),
        'duration': re.compile(DURATION_PATTERN),
        
        # Common
        'account': re.compile(ACCOUNT_PATTERN),
        'laycan': re.compile(LAYCAN_PATTERN),
        'date_range': re.compile(DATE_RANGE_PATTERN),
    }
    return patterns


# Compile patterns at module load
PATTERNS = compile_patterns()


def get_keyword_count(text: str, keywords: List[str]) -> int:
    """Count how many keywords appear in text."""
    count = 0
    for keyword_pattern in keywords:
        if re.search(keyword_pattern, text, re.IGNORECASE):
            count += 1
    return count
