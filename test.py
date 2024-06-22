import requests

BASE_URL = 'https://api.disneyapi.dev/'
character_name = input('Enter character name: ')
url = BASE_URL + 'character?name=' + character_name

response = requests.get(url)

if response.status_code == 200:
  character_data = response.json()
  if character_data and 'data' in character_data:
    for character in character_data['data']:
      if 'films' in character and isinstance(character['films'], list):
        films = character['films']
        print(f"Films associated with {character_name}:")
        for film in films:
            print(film)
      else:
        print(f"No films found for {character_name}")
  else:
    print(f"No character found with name: {character_name}")
else:
  print(f"Failed to fetch character. Status code: {response.status_code}")
