import requests
from credentials import credentials
from pprint import pprint

url = "https://api.amazon.com/auth/o2/token"

data = {
    "grant_type": "refresh_token",
    "refresh_token": credentials["refresh_token"],
    "client_id": credentials["client_id"],
    "client_secret": credentials["client_secret"],
}

response = requests.post(url, data=data)

pprint(response.json())

print("\n\nAccess Token: ", response.json()["access_token"])
