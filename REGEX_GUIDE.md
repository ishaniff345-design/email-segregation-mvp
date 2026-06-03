# Regex Guide (based on document patterns)

This guide lists the initial regexes that will be used for classification and extraction. Each regex is tied to an example from the document.

## 1. Account name
**Regex**
```
(?i)\b(?:ACC|A/C)\s+(?P<account>[A-Z0-9][A-Z0-9\s&.'-]+)
```
**Purpose**: Capture the account/company name.  
**Example input**: "ACC DAI AN OCEAN SHIPPING COMPANY LIMITED"  
**Example output**: "DAI AN OCEAN SHIPPING COMPANY LIMITED"  
**Source pattern from document**: "ACC DAI AN OCEAN SHIPPING COMPANY LIMITED"

## 2. Vessel name (MV or M/V)
**Regex**
```
(?i)\bM\/?V\.?\s+(?P<vessel>[A-Z0-9][A-Z0-9\s.'/-]+)
```
**Purpose**: Capture vessel name after MV or M/V.  
**Example input**: "MV SHENG AN HAI DWT 56564 OPEN XIAMEN"  
**Example output**: "SHENG AN HAI"  
**Source pattern from document**: "MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA"

## 3. Vessel size (DWT after keyword)
**Regex**
```
(?i)\bDWT\s*[:\-]?\s*(?P<size>[0-9][0-9,\.]*?)\b
```
**Purpose**: Capture DWT when it appears after the DWT keyword.  
**Example input**: "DWT 38,821.5 MT"  
**Example output**: "38,821.5"  
**Source pattern from document**: "MV DE SHENG HAI DWT 38,821.5 MT OPEN MUCURIPE"

## 4. Vessel size (K DWT format)
**Regex**
```
(?i)\b(?P<size>\d+(?:\.\d+)?)\s*K\s*DWT\b
```
**Purpose**: Capture vessel size in "38K DWT" format.  
**Example input**: "MV BLUE STAR (38K DWT) - OPEN 25 MAY GABES, TUNISIA"  
**Example output**: "38"  
**Source pattern from document**: "MV BLUE STAR (38K DWT) - OPEN 25 MAY GABES, TUNISIA"

## 5. Open port
**Regex**
```
(?i)\bOPEN\s+(?P<open_port>[A-Z][A-Z\s,.\'-/]+?)(?:\s+O\/A|\s+\d{1,2}|\s+ONW|$)
```
**Purpose**: Capture open port after OPEN.  
**Example input**: "OPEN VUNG ANG, VIETNAM 08-12 JUNE"  
**Example output**: "VUNG ANG, VIETNAM"  
**Source pattern from document**: "OPEN VUNG ANG, VIETNAM 08-12 JUNE"

## 6. Open date (O/A)
**Regex**
```
(?i)\bO\/A\s*(?P<open_date>\d{1,2}(?:ST|ND|RD|TH)?\s+[A-Z]{3,9}(?:\s+\d{4})?)\b
```
**Purpose**: Capture open date after O/A.  
**Example input**: "O/A 2ND JUNE 2026"  
**Example output**: "2ND JUNE 2026"  
**Source pattern from document**: "OPEN XIAMEN, CHINA O/A 2ND JUNE 2026"

## 7. Open date (ONW)
**Regex**
```
(?i)\b(?P<open_date>\d{1,2}(?:ST|ND|RD|TH)?\s+[A-Z]{3,9})\s+ONW\b
```
**Purpose**: Capture open date when followed by ONW.  
**Example input**: "1ST JUNE ONW"  
**Example output**: "1ST JUNE"  
**Source pattern from document**: "MV TRUE FRIEND/51K/ 09 - BEJAIA , 1ST JUNE ONW"

## 8. Date range (DD-DD MONTH [YEAR])
**Regex**
```
(?i)\b(?P<range>\d{1,2}\s*-\s*\d{1,2}\s+[A-Z]{3,9}(?:\s+\d{4})?)\b
```
**Purpose**: Capture date ranges like 24-25 MAY 2026 or 16-20 JULY.  
**Example input**: "24-25 MAY 2026"  
**Example output**: "24-25 MAY 2026"  
**Source pattern from document**: "O/A 24-25 MAY 2026"

## 9. Single date (day month [year])
**Regex**
```
(?i)\b(?P<date>\d{1,2}(?:ST|ND|RD|TH)?\s+[A-Z]{3,9}(?:\s+\d{4})?)\b
```
**Purpose**: Capture single dates like 1ST JUNE or 2ND JUNE 2026.  
**Example input**: "1ST JUNE"  
**Example output**: "1ST JUNE"  
**Source pattern from document**: "MV TRUE FRIEND/51K/ 09 - BEJAIA , 1ST JUNE ONW"

## 10. Laycan (LAYCAN or LC)
**Regex**
```
(?i)\b(?:LAYCAN|LC)\s*[:\-]?\s*(?P<laycan>[A-Z0-9 ,\-\/]+?)
```
**Purpose**: Capture laycan text for cargo lines.  
**Example input**: "LAYCAN: 16 -20 July"  
**Example output**: "16 -20 July"  
**Source pattern from document**: "LAYCAN: 16 -20 July"

## 11. Load port (VC)
**Regex**
```
(?i)\b(?:LOAD\s+PORT|POL|LP)\s*[:\-]?\s*(?P<loading_port>[A-Z][A-Z\s/+.]+)
```
**Purpose**: Capture loading port for Cargo VC.  
**Example input**: "LOAD PORT : KOH SI CHANG , THAILAND"  
**Example output**: "KOH SI CHANG , THAILAND"  
**Source pattern from document**: "LOAD PORT : KOH SI CHANG , THAILAND"

## 12. Discharge port (VC)
**Regex**
```
(?i)\b(?:DISCHARGE\s+PORT|POD|DP)\s*[:\-]?\s*(?P<discharge_port>[A-Z][A-Z\s/+.]+)
```
**Purpose**: Capture discharge port for Cargo VC.  
**Example input**: "DISCHARGE PORT: KANDLA + CHENNAI"  
**Example output**: "KANDLA + CHENNAI"  
**Source pattern from document**: "DISCHARGE PORT: KANDLA + CHENNAI"

## 13. Cargo quantity and name
**Regex**
```
(?i)\b(?P<quantity>\d[\d,.\s-]*?)\s*MTS?\s+(?P<cargo>[A-Z0-9][A-Z0-9\s\-/.]+)
```
**Purpose**: Capture cargo quantity and name from a VC line.  
**Example input**: "15,000 - 20,000 MTS 10PCT MOLOCHOPT"  
**Example output**: quantity="15,000 - 20,000", cargo="10PCT MOLOCHOPT"  
**Source pattern from document**: "15,000 - 20,000 MTS 10PCT MOLOCHOPT"

## 14. Cargo line with "Cargo:"
**Regex**
```
(?i)\bCargo\s*[:\-]?\s*(?P<cargo_line>.+)
```
**Purpose**: Capture cargo info when prefixed with "Cargo:".  
**Example input**: "Cargo:30,000 mts of Urea in bulk"  
**Example output**: "30,000 mts of Urea in bulk"  
**Source pattern from document**: "Cargo:30,000 mts of Urea in bulk"

## 15. Delivery port (TC)
**Regex**
```
(?i)\b(?:DELIVERY|DELY)\s*(?:TM|TO)?\s*(?P<delivery_port>[A-Z][A-Z\s/+.]+)
```
**Purpose**: Capture delivery port for Cargo TC.  
**Example input**: "DELIVERY TM VANCOUVER"  
**Example output**: "VANCOUVER"  
**Source pattern from document**: "DELIVERY TM VANCOUVER"

## 16. Redelivery port (TC)
**Regex**
```
(?i)\b(?:REDELIVERY|REDEL)\s*(?P<redelivery_port>[A-Z][A-Z\s/+.]+)
```
**Purpose**: Capture redelivery port for Cargo TC.  
**Example input**: "REDELIVERY CHITTAGONG"  
**Example output**: "CHITTAGONG"  
**Source pattern from document**: "REDELIVERY CHITTAGONG"

## 17. Duration (TC)
**Regex**
```
(?i)\bDURATION\s*[:\-]?\s*(?P<duration>(?:ABT\s*)?\d+\s*(?:-\s*\d+)?\s*DAYS?)\b
```
**Purpose**: Capture duration for Cargo TC.  
**Example input**: "DURATION ABT 30 DAYS WOG"  
**Example output**: "ABT 30 DAYS"  
**Source pattern from document**: "DURATION ABT 30 DAYS WOG"