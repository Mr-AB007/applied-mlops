# Day 10 — Feature Engineering: Scaling & Encoding (Java → Python)
**Topics:** feature scaling (StandardScaler/MinMaxScaler), encoding categorical variables, first real use of `census-income-prediction`

This is where your anchoring project properly kicks off — today's the first day you work with the *actual* census income dataset instead of `score.csv`/iris toy data. The goal isn't training a model yet (that's Day 11) — it's getting raw, messy real-world data into a shape a model can actually consume.

> **Scaffolding vs. learning code:** no scaffolding today, same as Day 9 — every line here is something you should understand, not just run.

---

## 1. Loading the dataset — `ucimlrepo`

The census income dataset (officially called "Adult" on UCI) is public but the raw file has no header row and marks missing values with a literal `" ?"` string — both easy to trip on. Skip that entirely with the `ucimlrepo` package, which pulls it with correct column names and types already set:

```bash
pip install ucimlrepo
```

```python
from ucimlrepo import fetch_ucirepo

adult = fetch_ucirepo(id=2)     # id=2 is the "Adult" / Census Income dataset specifically
X = adult.data.features          # DataFrame: all input columns (age, occupation, etc.)
y = adult.data.targets           # DataFrame: just the target column (income)

df = X.copy()
df["income"] = y
```

**Why the last line matters:** `fetch_ucirepo()` hands you features (`X`) and target (`y`) as two separate objects — that's the shape `model.fit(X, y)` eventually wants. But today's work (exploring, scaling, encoding) is easier with everything in one table: `df.info()`/`.describe()` show the full picture at once, and when you `dropna()` for missing values, you want a missing `income` label to count as a bad row too, same as a missing feature would. So `df["income"] = y` is just pasting the target back on as one more column for now — same idea as `user.setEmail(email)` on a Java DTO after construction. You'll split them apart again in Day 11, right before training, with `X = df.drop(columns=["income"])` / `y = df["income"]` — that's the shape the model actually needs.

**Check before moving on:** if you called `.dropna()` before combining `income` back into `df`, would that catch a row with a missing label? (No — which is exactly why the combine happens first.)

---

## 2. Why raw data isn't ready for a model

The census income dataset has a mix of column types: numeric (`age`, `hours-per-week`), and categorical (`occupation`, `education`, `marital-status`). Two problems stand in the way of feeding this straight into a model:

1. Models can't do math on strings — categorical columns need to become numbers (you saw a taste of this idea already).
2. Numeric columns are on wildly different scales — `age` might range 17–90, while `capital-gain` can range 0–99,999. Some algorithms (anything distance-based, or gradient-based like logistic regression) will let the large-range column dominate the model's learning simply because its numbers are bigger — not because it's actually more important.

**Java mapping:** think of scaling like normalizing units before a calculation — you wouldn't average "distance in meters" with "distance in kilometers" without converting first; the model has the same problem across columns.

**Check before moving on:** in your own words, why would an unscaled `capital-gain` column (0–99,999) distort a model more than `age` (17–90)?

---

## 3. Feature scaling — StandardScaler

`StandardScaler` transforms each numeric column to have mean 0 and standard deviation 1 — same shape of distribution, just rescaled.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numeric_cols = ["age", "hours-per-week", "capital-gain", "capital-loss"]

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
```

- `.fit()` calculates the mean/std from the data.
- `.transform()` applies the actual rescaling.
- `.fit_transform()` does both in one call — but only on **training** data. (You'll see next week why fitting the scaler on test data too is a subtle but common bug — it leaks information from data the model shouldn't have seen yet. For today, just know the rule: fit on train, transform both.)

**Video (StatQuest):** search "StatQuest Feature Scaling" — short one, watch the whole thing.

---

## 4. Encoding categorical variables — recap + applied to the real dataset

Same concept as before, now on real messy data with more categories per column (`education` alone has ~16 distinct values in this dataset).

```python
import pandas as pd

categorical_cols = ["occupation", "education", "marital-status", "sex"]

df_encoded = pd.get_dummies(df, columns=categorical_cols)
```

One thing you'll notice for the first time today: one-hot encoding a column with 16 categories creates 16 new columns. That's normal — this is why real feature sets can balloon to dozens or hundreds of columns even from a handful of original ones. Nothing to fix today, just something to notice.

**Check before moving on:** if `education` has 16 unique values, how many new columns does `pd.get_dummies()` create for it?

---

## 5. Putting it together — a full preprocessing pass

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo

# 1. Load and recombine (Section 1)
adult = fetch_ucirepo(id=2)
df = adult.data.features.copy()
df["income"] = adult.data.targets

# 2. Handle any missing values first (Day 5 skills — don't skip this)
df = df.dropna()

# 3. Scale numeric columns
numeric_cols = ["age", "hours-per-week", "capital-gain", "capital-loss"]
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# 4. Encode categorical columns
categorical_cols = ["occupation", "education", "marital-status", "sex"]
df_final = pd.get_dummies(df, columns=categorical_cols)

# 5. Save the processed result so Day 11 can pick up straight from here
df_final.to_csv("census_income_processed.csv", index=False)
```

Notice the order: handle missing data → scale → encode → save. Today ends with a clean CSV, not a trained model — Day 11 picks up from `census_income_processed.csv` directly.

---

## Today's Tasks

Folder: `applied-mlops/ml-fundamentals/day_10/` (or wherever your `census-income-prediction` project root lives)

1. **`explore_data.py`:**
   - Load the dataset with `fetch_ucirepo(id=2)` and recombine `X`/`y` into one `df` (Section 1).
   - Print `.info()` and `.describe()` to see column types and numeric ranges.
   - Print `.isnull().sum()` (Day 5 recap) — handle any missing values with `dropna()` or `fillna()`, your choice, and write a one-line comment on which you picked and why.

2. **`scale_features.py`:**
   - Pick the numeric columns and apply `StandardScaler`.
   - Print the `.mean()` and `.std()` of one scaled column before vs. after, to confirm it's now ~0 and ~1.

3. **`encode_features.py`:**
   - Apply `pd.get_dummies()` to the categorical columns.
   - Print `df.shape` before and after encoding — comment on how much the column count grew and why.

4. **`build_pipeline.py`:**
   - Combine steps 1–3 into one script, in the correct order (missing data → scale → encode).
   - Save the result to `census_income_processed.csv`.

**Time estimate:** 2 hours total.

---

**Tomorrow (Day 11 preview):** You load `census_income_processed.csv`, do the train/test split from Day 9 on it, train your first real `LogisticRegression` model on actual census income data, and evaluate it with the confusion matrix / precision / recall you already know how to read.