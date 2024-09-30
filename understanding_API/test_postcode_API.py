import requests
from pprint import pprint

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req)

print(f"Status code: {post_codes_req.status_code}")
print(f"Headers: {post_codes_req.headers}")
print(f"Content: {post_codes_req.content}")
print(f"JSON: {post_codes_req.json()}")
print(f"Data type of JSON: {type(post_codes_req.json())}")

pprint(post_codes_req.json())

data_dict = post_codes_req.json()['result']
print(f"Region: {data_dict['region']}")
