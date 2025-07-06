"""
CVS Health ML Engineer Setup Test
Test file to verify VS Code extensions are working correctly
"""

import sys
import datetime

def test_environment():
    """
    Test function to verify Python environment and extensions
    Returns system information and current timestamp
    """
    print("=== CVS Health ML Engineer Setup Test ===")
    print(f"Python version: {sys.version}")
    print(f"Test timestamp: {datetime.datetime.now()}")
    print("VS Code extensions working correctly! ✅")
    
    # Test basic data structure
    retail_data = {
        "store_id": 1001,
        "sales": [120.50, 89.75, 200.00],
        "products": ["aspirin", "vitamins", "bandages"]
    }
    
    return retail_data

if __name__ == "__main__":
    result = test_environment()
    print(f"Sample retail data: {result}")
    