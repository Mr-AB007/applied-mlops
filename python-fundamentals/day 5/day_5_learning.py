import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

#nan values automatically convert all values to fload even tough we use int
data = {"name": ["Anubhav", "Supriya", "Rakesh", "Priya"],
        "score": [70, np.nan, 55, 88]}
df = pd.DataFrame(data)

# print(df.isnull() )            # True/False mask, per cell
# print(df.isnull().sum())     # count of missing values, per column
# print(df["score"].isnull()) # just for one column

df_clean = df.dropna()  #drop the nan values rows
df_clean_values = df["score"].fillna(0)  #replace nan values with 0
df_clean_mean = df["score"].fillna(df["score"].mean()) #relace all nan with score mean(avg)

(df["score"] == np.nan) # ALWAYS returns False, even for NaN cells — classic bug


#============================================
#Merging/Joining DataFrames — like SQL JOINs
#============================================

students = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Anubhav", "Supriya", "Rakesh"]
})

scores = pd.DataFrame({
    "id": [1, 2, 4],
    "score": [70, 55, 88]
})

#Inner join (only matching ids — like SQL's default JOIN)

result_df = pd.merge(students, scores, on="id", how="inner") #id 4 and 3 is missing from both

#Left join
result_df = pd.merge(students,scores,on="id",how="left") #Rakesh has no matching score → filled with NaN automatically.
# how=	Behavior
# "inner"	Only rows matching in both (default)
# "left"	All rows from left, matched or NaN from right
# "right"	All rows from right, matched or NaN from left
# "outer"	All rows from both, NaN where no match
result_df = pd.merge(students,scores,on="id",how="outer")
# print(result_df)

#Concatenating (stacking rows, no key needed — like combining two lists)

batch1 = pd.DataFrame({"Name":["AB"],"score":[70]})
batch2 = pd.DataFrame({"Name":["BC"],"score":[55]})

result = pd.concat([batch1,batch2],ignore_index=True) #it just combines two dataset like java appen,
# igore_index create new index
# print(result)

#=================================================
# 3. Visualization — matplotlib & seaborn basics
#=================================================

import matplotlib.pyplot as plt


#matplotlib — the base library (lower-level, more manual)
# df["score"].plot(kind="hist")
# plt.title("Score Distribution")
# plt.xlabel("Score")
# plt.ylabel("Count")
# plt.show()

import seaborn as sns

sns.histplot(df["score"])
plt.show()

sns.boxplot(x=df["score"])       # good for spotting outliers
plt.show()

sns.scatterplot(x="score", y="score", data=df)  # example — normally two different columns
plt.show()