import pandas as pd
df = pd.read_csv("YT_pokemon.csv", index_col="Name")


#SELECTTION BY COLUMN
# print(df["Name"]) >>> since we are using names as index we cant use this
print(df.index)
# print(df["Name"].to_string()) #be careful if u have a lot of data
print(df["Height"])
print(df["Weight"])


print(df.reset_index()[["Name", "Height", "Weight"]]) # multiple columns




#SELECTION BY ROW/ROWS
# print(df.loc[1]) # we cant use this becoz Name is the index 
print(df.loc["Pikachu"])
print()
print(df.loc["Charizard", ["Height", "Weight"]]) # we want only two columns

print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])  #everything between charizard and blastoise inclusive


print()

print(df.iloc[0:11]) # 0 is inclusieve and 11 is exlusive 
print(df.iloc[0:11:2, 0:3]) #this ll return only 0-11 but only alternates and 0:3 (column indicies) means only first 3 rows so it will print only 3 rows



#finding a pokemon
pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} doesnt exist in the list")