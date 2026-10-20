import pandas as pd
# Filtering: keeping the rows that match a condition
df = pd.read_csv("YT_pokemon.csv")

print(df)

tall_pokemon = df[df["Height"] >= 2]
print(tall_pokemon)

heavy_pokemon = df[df["Weight"] >= 100]
print(heavy_pokemon)

legendary_pokemon = df[df["Legendary"] == 1] # or we can write True instead of 1
print(legendary_pokemon)

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

ff = df[(df["Type1"]=="Fire") & (df["Type2"] == "Flying")]
print(ff)