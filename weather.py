import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lang":"en","lon":"<required>","lat":"<required>"}

headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': "96e378cea5msh261b20bbf9c9ba8p1d5686jsndec440cbf6f2"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
