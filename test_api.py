#!/usr/bin/env python
"""
Quick test script to verify the API works correctly.
Run: python test_api.py
"""

import json
import requests

BASE_URL = "http://127.0.0.1:8000"

# Test cases
test_cases = [
    {
        "name": "Tonnage - Simple",
        "email": "MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026",
        "expected_category": "tonnage"
    },
    {
        "name": "Cargo VC",
        "email": "15,000 - 20,000 MTS MOLOCHOPT LOAD PORT: KOH SI CHANG, THAILAND DISCHARGE PORT: KANDLA + CHENNAI LAYCAN: MID JULY 2026",
        "expected_category": "cargo_vc"
    },
    {
        "name": "Cargo TC",
        "email": "ACC DAI AN OCEAN SHIPPING COMPANY LIMITED DELIVERY TM VANCOUVER REDELIVERY CHITTAGONG DURATION ABT 30 DAYS",
        "expected_category": "cargo_tc"
    }
]

def test_api():
    print("Testing Email Segregation API\n")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print("-" * 60)
        
        try:
            response = requests.post(
                f"{BASE_URL}/extract",
                json={"email_text": test["email"]},
                timeout=5
            )
            
            if response.status_code != 200:
                print(f"❌ FAILED: HTTP {response.status_code}")
                failed += 1
                continue
            
            result = response.json()
            
            # Check category
            if result["category"] == test["expected_category"]:
                print(f"✓ Category: {result['category']}")
            else:
                print(f"✗ Category: Expected {test['expected_category']}, got {result['category']}")
            
            # Show confidence
            print(f"✓ Confidence: {result['confidence']*100:.0f}%")
            
            # Show extracted data
            if result["data"]:
                print(f"✓ Extracted fields: {len(result['data'])} fields")
                for key, value in result["data"].items():
                    print(f"  - {key}: {value[:50]}..." if len(str(value)) > 50 else f"  - {key}: {value}")
            else:
                print("  No data extracted")
            
            # Check if category matches
            if result["category"] == test["expected_category"]:
                passed += 1
                print("✓ TEST PASSED")
            else:
                failed += 1
                print("✗ TEST FAILED")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ FAILED: Cannot connect to {BASE_URL}")
            failed += 1
        except Exception as e:
            print(f"❌ FAILED: {str(e)}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"\nResults: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0

if __name__ == "__main__":
    success = test_api()
    exit(0 if success else 1)
