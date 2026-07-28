import pandas as pd

df = pd.read_csv("../score.csv")
# print(df.head())
# print(df.describe())
# print(df[df["score"] > 80])


#Add a new column grade where score >= 90 → "A", >= 75 → "B", else "C"

# Using array comprehension

df["grade"] = ["A" if score >= 90 else "B" if score >= 75 else "C" for score in df["score"]]

#using apply function
def get_garde(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

df["garde_apply"] = df["score"].apply(get_garde)
# print(df)

#Group by city with average score
avg = df.groupby("city")["score"].mean()

# Comparison: a plain loop is verbose but explicit and easy to debug step-by-step;
# a list comprehension is faster to write and more "Pythonic" for simple filters;
# pandas boolean filtering is the natural choice for real datasets since it's
# vectorized (no explicit loop) and integrates directly with DataFrame operations.
# using loop
for score in df["score"]:
    if score > 80:
        print(score)

# using  list comprehension

scores =[ score for score in df["score"] if score > 80]
print(f"Scores_arry : {scores}")

panda_scores  = df["score"][df["score"] > 80]

print(f"Pandas Scores_arry : {panda_scores}")