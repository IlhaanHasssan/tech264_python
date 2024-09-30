import json
import os
import sys
import yaml

source_content = None
# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library
yaml_data = yaml.dump(source_content)
print(yaml_data)
# 2. Save the YAML into a new file with the name for it received as a argument

# try:
#     with open(yaml_file_path, "r") as yaml_file:
#         yaml_obj = yaml.load(yaml_file, Loader=yaml.FullLoader)
#         print(yaml_obj)
# except FileNotFoundError:
#     print(f"File not found: {yaml_file_path}")

# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
if not len(sys.argv) > 2:
    print(yaml_data)
    sys.exit(1)
#
# if len(sys.argv) > 2 and not os.path.exists(sys.argv[2]):
#     target_file = sys.argv[2]
#     print(f"Target file: {target_file}")
#     with open(f"{target_file}.yaml", "w") as yaml_file:
#         yaml.dump(json_data, yaml_file)
# else:
#     yaml_obj = yaml.dump(json_data)
#     print(yaml_obj)

# 2.2 Check the target file doesn't already exist
# using 'and not' to check this in the code above
if os.path.exists(sys.argv[2]):
        print(f"Error: The file '{sys.argv[2]}' already exists. Please select a different file name.")
# 2.3 If previous conditions not met, then save YAML file
else:
    with open(sys.argv[2], 'w') as yaml_file:
        yaml_file.write(yaml_data)