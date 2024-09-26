# What is encoding vs serialising (very quick, two or three dot points to understand the difference)?
# Encoding refers to converting data from one format to another, often involving character encoding (e.g., UTF-8, ASCII).
# Use Case: When dealing with text data, encoding ensures that characters are represented in a consistent and compatible way across different systems.
# Example: Converting special characters (like accented letters) into their corresponding byte representations (e.g., converting “é” to %C3%A9 in URL encoding).
#Serialising means converting complex data structures (such as objects or dictionaries) into a format that can be easily stored, transmitted, or reconstructed.
# Use Case: Serialization is common when working with data storage (e.g., saving objects to files) or communication (e.g., sending data over a network).
# Example: Converting a Python dictionary into a JSON string or writing it to a binary file.

# Work out which one of them are you doing with the subtasks below
#We are doing serialising
# Starting code:
import json
# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}


# Convert the dictionary to a JSON-formatted string
json_string = json.dumps(servers_dict)

print("This is the JSON-formatted string:")
print(json_string)

# Write the dictionary to a JSON file
with open("servers.json", "w") as json_file: #with open("servers.json", "w") as json_file: opens a file named “servers.json” in write mode ("w")
    json.dump(servers_dict, json_file, indent=4)

print("Data will be sent to servers.json.")


# Subtasks:
#
# Convert this Python dictionary into a JSON-formatted string
# Convert this Python dictionary to a JSON file
# Extra guidance:
#
# Use the json library
# Write any other code necessary to test things converted correctly