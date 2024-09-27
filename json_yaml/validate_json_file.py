import os
import sys
import json

if len(sys.argv) > 1:
    # Check if the file exists
    if os.path.exists(sys.argv[1]):
        # Open the file for reading
        with open(sys.argv[1], "r") as file:
            try:
                # Attempt to parse the JSON file
                json.load(file)
                print("JSON file is valid!")
            except json.JSONDecodeError:
                print("ERROR: The file does not contain valid JSON.")
    else:
        # Alert the user that the specified file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    print("ERROR: No JSON file was specified to check")
    print(f"Usage: {sys.argv[0]} <JSON filename>")
