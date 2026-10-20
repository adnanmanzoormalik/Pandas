import pandas as pd
#Aggregation functions >>> often used eith groupby()

df = pd.read_csv("YT_pokemon.csv")
print(df)



#aggregate functions for the whole data
print(df.mean(numeric_only=True)) # we cant use mean() for non numeric values

print(df.sum(numeric_only=True))

print(df.min(numeric_only=True))

print(df.max(numeric_only=True))

print(df.count())



#aggregate functions for a single column
print(df["Height"].mean()) # we cant use mean() for non numeric values

print(df["Height"].sum())

print(df["Height"].min())

print(df["Height"].max())

print(df["Height"].count())




#groupby()

group = df.groupby('Type1')
print(group) # this ll print <pandas.core.groupby.generic.DataFrameGroupBy object at 0x10a0fee80>

print(group["Height"].mean())

print(group["Height"].sum())

print(group["Height"].min())

print(group["Height"].max())

print(group["Height"].count())