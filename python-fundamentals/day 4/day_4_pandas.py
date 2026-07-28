import pandas as pd

#Pandas — DataFrames (like an in-memory spreadsheet/SQL table)
data = {
    "name": ["Anubhav", "Supriya", "Rakesh"],
    "score": [70, 92, 55],
    "city": ["Patna", "Pune", "Delhi"]
}

df = pd.DataFrame(data)
# print(df)

#using dataframes to import CSV and work

df = pd.read_csv("score.csv")

# print(df.head()) # first 5 rows
# print("----INFO----")
# print(df.info() )       # column types, non-null counts
# print("----DESCRIBE----")
# print(df.describe())    # statistical summary (mean, min, max, etc.) for numeric columns
# print("----SHAPE----")
# print(df.shape )       # (rows, columns)
# print("----COLUMS----")
# print(df.columns)  # list of column names

#Selecting one column

# print(df["score"]  ) # single column (returns a Series)

#print(df[["name", "score"]])     # multiple columns (returns a DataFrame)
#print(df.iloc[0])             # first row, by position
#print(df.loc[0, "name"])        # specific cell, by label


#Filtering (comprehensions-thinking transfers directly)

# Rows where score > 80
high_scorers = df[df["score"] > 80]

# Multiple conditions - use & and |, NOT 'and'/'or'
result = df[(df["score"] > 60) & (df["city"] == "Pune")]
# print(result)


# Aggregating — like SQL's GROUP BY
df.groupby("city")["score"].mean()     # average score per city
df["score"].sum()                       # total of a column
df.sort_values("score", ascending=False) # sort rows by a column


#Adding/modifying columns
df["Passed"] = df["score"] > 80          # new boolean column
df["score_doubled"] = df["score"] * 2     # new numeric column


df.to_csv("updated_score.csv", index=False) #writing back to csv