# Shipping Email Segregation - Document Analysis

## Business problem
The document asks for a system that reads incoming shipping emails, classifies them, and extracts key commercial information. The extracted data should be stored in a structured format to support searching, matching, and business opportunity generation. The solution must avoid third-party LLM APIs and rely on rule-based or alternative methods.

## Email categories
1. **Tonnage (Open Vessels)** - emails describing vessel availability.
2. **Cargo VC (Voyage Charter Cargo)** - emails describing cargo requirements for a voyage.
3. **Cargo TC (Time Charter Cargo)** - emails describing time charter requirements.

## Pattern analysis
**Tonnage**
- Key indicators: OPEN, MV/M/V, DWT, O/A, ONW, VSL PARTICULAR.
- Structure often includes vessel name + DWT + OPEN port + open date.
- Examples:
  - "SARONIC CHAMPION (93K ...) - OPEN VUNG ANG, VIETNAM 08-12 JUNE"
  - "MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026"
  - "MV TRUE FRIEND/51K/ 09 - BEJAIA , 1ST JUNE ONW"
  - "MV BLUE STAR (38K DWT) - OPEN 25 MAY GABES, TUNISIA"

**Cargo VC**
- Key indicators: LOAD PORT, DISCHARGE PORT, POL, POD, LP, DP, LAYCAN, LC, MTS/MT.
- Structure often includes quantity + cargo name + loading port + discharge port + laycan.
- Examples:
  - "15,000 - 20,000 MTS 10PCT MOLOCHOPT"
  - "LOAD PORT : KOH SI CHANG , THAILAND"
  - "DISCHARGE PORT: KANDLA + CHENNAI"
  - "LP:Bushehr / DP: Doha"
  - "Cargo:30,000 mts of Urea in bulk"
  - "LAYCAN: 16 -20 July"

**Cargo TC**
- Key indicators: TCT, DELIVERY, REDELIVERY, DURATION, ACC, A/C, LC.
- Structure often includes account + delivery port + redelivery port + duration + laycan.
- Examples:
  - "ACC DAI AN OCEAN SHIPPING COMPANY LIMITED"
  - "DELIVERY TM VANCOUVER"
  - "REDELIVERY CHITTAGONG"
  - "DURATION ABT 30 DAYS WOG"
  - "LC 10 -17 JUNE"

## Why regex
The document provides consistent keyword patterns and semi-structured lines. Regex can reliably locate these keywords and capture fields without external AI services.

## Why rule-based classification
Rule-based scoring is transparent, simple to explain, and easy to tune. It aligns with the requirement to avoid external LLM APIs.

## Edge cases
- Multiple vessels or cargoes in one email.
- Multiple ports in a single line using "+" or "or".
- Laycan written as "LC" without the word "LAYCAN".
- Dates shown as ranges ("24-25 MAY 2026") or phrases ("FULL MAY", "MID JULY 2026").
- Open date embedded with "ONW" or "O/A".
- Noise from signatures and long vessel particulars.

## Future improvements (from document)
- Automatic matching of suitable vessels and cargoes.
- Duplicate email detection.
- Customer and broker-wise tracking.
- Market opportunity alerts.
- Integration with voyage and chartering workflows.