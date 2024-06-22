import requests
import pandas as pd
import sqlalchemy as db

response = requests.get('https://api.disneyapi.dev/character/25')
characters = response.json()['data']
#character_data = characters[0]

dict1 = {}
for key in ["_id", "films"]:
  dict1[key] = characters[key]

df = pd.DataFrame.from_dict(dict1)
engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('characters', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM characters;")).fetchall()
   print(pd.DataFrame(query_result))