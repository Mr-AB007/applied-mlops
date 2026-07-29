# Day 5 — Python for Data (Java → Python)
**Topics:** Missing Data, Merging/Joining DataFrames, Intro to Visualization (matplotlib/seaborn)

This is the last "core data handling" day before you move into actual model training next week. Everything here is stuff you'll do on *every* real dataset before it's usable — real data is never as clean as `score.csv`.

---

## 1. Missing Data — pandas' `NaN`

Real datasets almost always have gaps — a sensor that didn't log a reading, a survey question someone skipped, a join that didn't find a match. Pandas represents "missing" using a special float value: `NaN` (Not a Number), from NumPy (`np.nan`).

There's no real Java equivalent here — the closest concept is `null`, but `NaN` behaves differently: it's a float value, and critically, `NaN != NaN` (comparing it to itself returns `False`), which is why you never check for missing values with `== NaN`.

### Detecting missing values
```python
import pandas as pd
import numpy as np

data = {"name": ["Anubhav", "Supriya", "Rakesh", "Priya"],
        "score": [70, np.nan, 55, 88]}
df = pd.DataFrame(data)

df.isnull()             # True/False mask, per cell
df.isnull().sum()        # count of missing values, per column
df["score"].isnull()     # just for one column
```

### Handling missing values — three common strategies

**1. Drop rows with any missing values:**
```python
df_clean = df.dropna()
```

**2. Fill with a default value:**
```python
df["score"] = df["score"].fillna(0)
```

**3. Fill with a computed value (much more common in real ML prep — e.g., mean imputation):**
```python
df["score"] = df["score"].fillna(df["score"].mean())
```

**Never do this:**
```python
df["score"] == np.nan     # ALWAYS returns False, even for NaN cells — classic bug
```
Always use `.isnull()` / `.notnull()`, never a direct equality check.

---

## 2. Merging/Joining DataFrames — like SQL JOINs

If you've written SQL joins (or Java code combining data from two `Map`/`List` sources by a common key), `pd.merge()` is the same idea.

```python
students = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Anubhav", "Supriya", "Rakesh"]
})

scores = pd.DataFrame({
    "id": [1, 2, 4],
    "score": [70, 92, 55]
})
```

### Inner join (only matching ids — like SQL's default `JOIN`)
```python
result = pd.merge(students, scores, on="id", how="inner")
```
```
   id     name  score
0   1  Anubhav     70
1   2  Supriya     92
```
Note: id `3` (no score) and id `4` (no student) both got dropped — only ids present in *both* tables survive.

### Left join (keep everything from the left table, like SQL's `LEFT JOIN`)
```python
result = pd.merge(students, scores, on="id", how="left")
```
```
   id     name  score
0   1  Anubhav   70.0
1   2  Supriya   92.0
2   3   Rakesh    NaN
```
Rakesh has no matching score → filled with `NaN` automatically.

### Other join types
| `how=` | Behavior |
|---|---|
| `"inner"` | Only rows matching in both (default) |
| `"left"` | All rows from left, matched or NaN from right |
| `"right"` | All rows from right, matched or NaN from left |
| `"outer"` | All rows from both, NaN where no match |

### Concatenating (stacking rows, no key needed — like combining two lists)
```python
batch1 = pd.DataFrame({"name": ["A"], "score": [70]})
batch2 = pd.DataFrame({"name": ["B"], "score": [90]})
combined = pd.concat([batch1, batch2], ignore_index=True)
```
Use `merge` when you're **combining columns** based on a shared key; use `concat` when you're **stacking rows** from datasets with the same columns (e.g., combining daily log files into one DataFrame).

---

## 3. Visualization — matplotlib & seaborn basics

You won't do deep visualization work in MLOps day-to-day, but you'll constantly use quick plots to sanity-check data (distributions, missing patterns, trends) before feeding it into a model.

### matplotlib — the base library (lower-level, more manual)
```python
import matplotlib.pyplot as plt

df["score"].plot(kind="hist")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Count")
plt.show()
```

### seaborn — built on top of matplotlib, nicer defaults, less code for common plots
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df["score"])
plt.show()

sns.boxplot(x=df["score"])       # good for spotting outliers
plt.show()

sns.scatterplot(x="score", y="score", data=df)  # example — normally two different columns
plt.show()
```

**Rule of thumb:** use matplotlib when you need fine-grained control; use seaborn when you want a good-looking plot in one line for quick data exploration. Most people default to seaborn for exploration and drop to matplotlib only for customization.

---

## Today's Tasks

1. **Missing data practice** in `missing_data.py`:
   - Create a DataFrame with at least 5 rows and one column containing 2 missing values (`np.nan`).
   - Print `.isnull().sum()` to confirm the count.
   - Create one version with `dropna()` and print it.
   - Create another version with `fillna()` using the column's mean, and print it.

2. **Merge practice** in `merge_practice.py`:
   - Create two DataFrames: one with `id, name` (at least 4 rows) and one with `id, score` (at least 4 rows, with at least one non-matching `id` in each).
   - Perform an `inner` join and print the result.
   - Perform a `left` join and print the result — observe where `NaN` appears.
   - Write one comment explaining, in your own words, why the row counts differ between the two joins.

3. **Visualization practice** in `visualize_practice.py`:
   - Using your `score.csv` (or updated_scores.csv) from Day 4, plot a histogram of the `score` column using `seaborn`.
   - Plot a boxplot of the same column.
   - Save one of the plots to a file instead of just showing it: `plt.savefig("score_distribution.png")`.

**Time estimate:** 2 hours total.

---

**Tomorrow (Week 2 preview):** You'll shift out of pure data-handling and into your first taste of actual MLOps tooling — starting with Docker fundamentals (containerizing a simple Python app), since this is likely to move faster for you given your existing backend/deployment experience.
