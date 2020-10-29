import requests


url = "https://api.opensea.io/wyvern/v1/orders"

querystring = {"token_id":"11150", 'limit': 20}

response = requests.request("GET", url, params=querystring)

print(response.text)