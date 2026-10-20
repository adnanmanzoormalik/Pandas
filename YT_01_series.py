import pandas as pd

print(pd.__version__)


# Series: 1 dimensional labeled array
data = [100,102,104,200,202]

series = pd.Series(data, index=["a","b","c","d","e"])
print(series)
# we ll get a valueerror if we got write enough indexes i.e equal to the number of elements in the series

print(series.loc['c'])
# we get a key error if we dont a proper index

series.loc['c'] = 101
print(series.loc['c'])


print(series.iloc[0]) # integer location

print(series[series >= 200])

calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}

series1 = pd.Series(calories)
print(series1)
print(series1.loc["Day 1"])

print(series1)

print(series1[series1<2000])

data = ["Adnan", "Manzoor", "Asrar", "Bakhti", "Saad"]
series2 = pd.Series(data, index=[1,2,3,4,5])
print(series2)














