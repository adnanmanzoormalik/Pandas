import pandas as pd
# DATA CLEANING: fixing or removing incomplete, incorrect or irrelevant data


df = pd.read_csv("YT_pokemon.csv")


#drop irrelevant columns
df = df.drop(columns=["No"])
print(df)


#handle missing data
# df = df.dropna(subset=["Type2"])
# print(df)

df = df.fillna({"Type2": "None"})
print(df)


#fic inconsistent values
df["Type1"] = df['Type1'].replace({"Grass": "GRASS", "Fire": "FIRE", "Water":"WATER"})
print(df.to_string())




#standardize text
df["Name"] = df["Name"].str.lower()
print(df)

df["Legendary"] = df["Legendary"].astype(bool)
print(df)


#remove duplicate values
df = df.drop_duplicates()
print(df)