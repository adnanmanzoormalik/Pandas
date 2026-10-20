import pandas as pd

df = pd.read_csv("YT_pokemon.csv")
print(df)

print(df.to_string())


df = pd.read_json("YT_pokemon.json")
print(df)
print(df.to_string())