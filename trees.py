

# Test a basic request

# user = "https://api.digitalhumani.com/tree"
# header = {
#     "Key": "X-Api-Key",
#     "Value": "mBzbK2u7L5vx4O0O3CMePRq1I49wi7wpqhMM8qleTSjGo5WG",
#     "treeCount": "1",
#     "enterpriseId": "a75b1fbf",
#     "projectId": "96666666",
#     "user": "test_user_1"
# }

# user = "https://api.digitalhumani.com/user/whoami"
# header = {
#     'Accepts': 'application/json' 
# }
# auth = HTTPBasicAuth('X-Api-Key', 'mBzbK2u7L5vx4O0O3CMePRq1I49wi7wpqhMM8qleTSjGo5WG')

# r = requests.get(user, headers=header, auth=auth)

# print(r)

import requests
import os

# Get the API key from an environment variable
api_key = 'mBzbK2u7L5vx4O0O3CMePRq1I49wi7wpqhMM8qleTSjGo5WG'

# The base URI for all requests
base_uri = "https://api.digitalhumani.com/"

# Set the custom header to include the API key
# headers = {'X-Api-Key': api_key}

# h = requests.get(f'{base_uri}', headers=headers)
# print(h)

s = requests.session()
headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': api_key,
}

response = s.post(f'{base_uri}tree', headers=headers, json= {
    "treeCount": 1,
    "enterpriseId": "a75b1fbf",
    "projectId": "96666666",
    "user": "test_user_1"
    })

# print(response.status_code)
# print(response.json())


h = requests.get(f'{base_uri}tree?enterpriseId=a75b1fbf&user=test_user_1', headers=headers)
# print(h)
# print(h.json())
j = h.json()
print(f'Thank You! You have planted 1 tree in Khasi Hills, India. Total Trees planted : {j["count"]}')