# Data Frame: tabular data structure with rows and columns
import pandas as pd
data = {
    "Name": ["Adnan", "Asrar", "Saad"],
    "Age" : [25,30,3]
}

df = pd.DataFrame(data, index=['Employee 1','Employee 2','Employee 3'])

print(df)

print(df.loc['Employee 1'])
print()
print(df.iloc[2])


#add a new column
df["Job"] = ["Developer", "Doctor", "Student"]
print(df)



#add a new row
new_row = pd.DataFrame([
    {
        "Name": "Sandy",
        "Age":28,
        "Job" : "Engineer"
     }
    ], index=["Employee 4"])
df = pd.concat([df, new_row])

print(df)

print()
# add new rows
new_rows = pd.DataFrame([
    {
        "Name": "Zaira",
        "Age":21,
        "Job" : "Nurse"
    },
    {
        "Name": "Omais",
        "Age":23,
        "Job" : "Manager"  
    },
    {
        "Name": "Jasleen",
        "Age":22,
        "Job" : "Developer"
    }
], index=["Employee 5", "Employee 6", "Employee 7"])

df = pd.concat([df, new_rows])
print(df)