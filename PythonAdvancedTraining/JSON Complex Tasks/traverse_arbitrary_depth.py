# Task: Write a recursive function to find and print the value of the deepest key.
import json

data = {
    "root": {
        "level1": {
            "level2": {
                "level3": {
                    "value": 42
                }
            }
        }
    }
}

def recursive_depth(d):
    for key, value in d.items():
        if isinstance(value, dict):
            recursive_depth(value)
        else:
            print(f"{key}: {value}")
            
recursive_depth(data)