import requests

url = 'https://api.citybik.es/v2/networks'
data = {
  'name': 'El Paso BCycle: Cleveland Square',
  'location':{
    'latitude': 31.759517,
    'longitude': -106.491605
  }
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Station added successfully!")
    print(f"Status code: {response.status_code}")
    print(response.json())
else:
    print("Failed to add station. Status code:", response.status_code)

#it is on their map now! wow!

url_get = 'https://api.citybik.es/v2/networks/bicing'

response_get = requests.get(url_get)

print(response_get.json())