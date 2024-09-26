import json

# Read the JSON data from servers.json
with open("servers.json", "r") as json_file:
    servers = json.load(json_file)

# Print the type of the resulting dictionary
print("Type of 'servers':", type(servers))

# Print dictionary records for keys "server1" and "server2"
print("Record for 'server1':", servers["server1"])
print("Record for 'server2':", servers["server2"])

# Print all keys and values
for key, value in servers.items():
    print(f"Key and value: '{key}' =", json.dumps(value))
    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' =", sub_value)
