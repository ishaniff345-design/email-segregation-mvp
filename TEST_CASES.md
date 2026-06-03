# Test Cases for Email Segregation

This document contains 10+ test cases derived from the shipping email document. Paste these into the UI to test the system.

## Test Case 1: Tonnage - Simple
**Category**: Tonnage  
**Expected Confidence**: 70%+

```
MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026
```

Expected:
- vessel_name: SHENG AN HAI
- vessel_size: 56564
- open_port: XIAMEN, CHINA
- open_date: 2ND JUNE 2026

## Test Case 2: Tonnage - K Format
**Category**: Tonnage  
**Expected Confidence**: 70%+

```
MV BLUE STAR (38K DWT) - OPEN 25 MAY GABES, TUNISIA
```

Expected:
- vessel_name: BLUE STAR
- vessel_size: 38K
- open_port: GABES, TUNISIA
- open_date: 25 MAY

## Test Case 3: Cargo VC
**Category**: Cargo VC  
**Expected Confidence**: 75%+

```
15,000 - 20,000 MTS 10PCT MOLOCHOPT
LOAD PORT : KOH SI CHANG , THAILAND
DISCHARGE PORT: KANDLA + CHENNAI
LAYCAN: MID JULY 2026
```

Expected:
- cargo_name: 10PCT MOLOCHOPT
- loading_port: KOH SI CHANG , THAILAND
- discharge_port: KANDLA + CHENNAI
- laycan: MID JULY 2026

## Test Case 4: Cargo VC - POL/POD
**Category**: Cargo VC  
**Expected Confidence**: 75%+

```
Cargo:30,000 mts of Urea in bulk
POL: BIK
POD: Iskenderun or Durban
LAYCAN: 16 -20 July
```

Expected:
- cargo_name: 30,000 mts of Urea in bulk
- loading_port: BIK
- discharge_port: Iskenderun or Durban
- laycan: 16 -20 July

## Test Case 5: Cargo TC
**Category**: Cargo TC  
**Expected Confidence**: 80%+

```
ACC DAI AN OCEAN SHIPPING COMPANY LIMITED
DELIVERY TM VANCOUVER
REDELIVERY CHITTAGONG
DURATION ABT 30 DAYS WOG
LC 10 -17 JUNE
```

Expected:
- account_name: DAI AN OCEAN SHIPPING COMPANY LIMITED
- delivery_port: VANCOUVER
- redelivery_port: CHITTAGONG
- duration: ABT 30 DAYS
- laycan: 10 -17 JUNE

## Test Case 6: Unknown
**Category**: Unknown  
**Expected Confidence**: 0%

```
Hi team,
Just a reminder that we have a meeting tomorrow at 2 PM.
Please bring your documents.
Thanks
```

Expected:
- No data extracted
- Category shows "Unknown"

## Testing Instructions

1. Copy one email text
2. Paste into textarea
3. Click "Extract & Classify"
4. Verify results match expected values
5. Check confidence is in expected range

## Success Criteria

✅ Tonnage: Keywords OPEN, MV, DWT detected
✅ Cargo VC: Keywords LOAD PORT, DISCHARGE PORT detected
✅ Cargo TC: Keywords DELIVERY, REDELIVERY, ACC detected
✅ Confidence: Score 0-100%
✅ Fields: Extracted values accurate