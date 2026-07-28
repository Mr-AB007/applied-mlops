# Day 4 — Python for Data (Java → Python)
**Topics:** NumPy Arrays, Pandas DataFrames, Filtering & Aggregating Data

This is the first day that moves from "Python the language" into "Python for ML" — everything from here on is the actual daily toolkit you'll use for data prep, feature engineering, and model input pipelines.

---

## 1. NumPy — Fast arrays for numeric data

Python's built-in `list` is flexible but slow for heavy numeric work (it stores generic objects, with overhead per element). NumPy's `ndarray` is the closest thing to Java's primitive arrays (`int[]`, `double[]`) — fixed type, packed in memory, and vectorized (operations apply to the whole array at once, no manual loop needed).

```python
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros(5)          # [0. 0. 0. 0. 0.]
ones = np.ones((2, 3))        # 2x3 matrix of 1s
range_arr = np.arange(0, 10, 2)   # [0 2 4 6 8]
```

### Vectorized operations — the big shift from Java

In Java, applying a math operation to every element requires a loop:
```java
// Java
for (int i = 0; i < arr.length; i++) {
    arr[i] = arr[i] * 2;
}
```

In NumPy, the operation applies to the entire array directly — no loop:
```python
arr = np.array([1, 2, 3, 4, 5])
doubled = arr * 2          # [2 4 6 8 10]
squared = arr ** 2         # [1 4 9 16 25]
added = arr + 10           # [11 12 13 14 15]
```
This is called **vectorization**, and it's not just shorter syntax — it's dramatically faster than looping, because NumPy runs the operation in optimized C code under the hood rather than Python's interpreter loop.

### Useful array operations
```python
arr = np.array([3, 12, 7, 45, 9, 22])

arr.sum()        # 98
arr.mean()       # 16.33
arr.max()        # 45
arr.min()        # 3
arr.sort()       # sorts in place
arr[arr > 10]    # filtering: [12 45 22] — array of elements matching condition
```

### 2D arrays (matrices) — like Java's `int[][]`
```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)     # (2, 3) -> 2 rows, 3 columns
print(matrix[0][1])     # 2
print(matrix[:, 1])     # column 1 across all rows -> [2 5]
```

---

## 2. Pandas — DataFrames (think: an in-memory spreadsheet/SQL table)

If NumPy is Java's arrays, Pandas is closer to a **List<Map<String,Object>>** or an in-memory database table — labeled rows and columns, mixed data types per column, built for tabular data (exactly what CSV files contain).

```python
import pandas as pd

data = {
    "name": ["Anubhav", "Supriya", "Rakesh"],
    "score": [70, 92, 55],
    "city": ["Patna", "Pune", "Delhi"]
}
df = pd.DataFrame(data)
print(df)
```
Output:
```
      name  score   city
0  Anubhav     70  Patna
1  Supriya     92   Pune
2   Rakesh     55  Delhi
```

### Reading directly from CSV (this replaces the raw `csv` module you used on Day 3)
```python
df = pd.read_csv("score.csv")
```
One line, versus manually opening the file, wrapping in `csv.reader`/`DictReader`, and looping — pandas handles all of that internally.

### Inspecting a DataFrame
```python
df.head()        # first 5 rows
df.info()        # column types, non-null counts
df.describe()    # statistical summary (mean, min, max, etc.) for numeric columns
df.shape         # (rows, columns)
df.columns       # list of column names
```

### Selecting columns and rows
```python
df["score"]              # single column (returns a Series)
df[["name", "score"]]     # multiple columns (returns a DataFrame)
df.iloc[0]                # first row, by position
df.loc[0, "name"]          # specific cell, by label
```

### Filtering — this is where comprehensions-thinking transfers directly
```python
# Rows where score > 80
high_scorers = df[df["score"] > 80]

# Multiple conditions - use & and |, NOT 'and'/'or'
result = df[(df["score"] > 60) & (df["city"] == "Pune")]
```
Note: pandas requires `&` / `|` instead of `and` / `or`, and each condition needs its own parentheses — a common early mistake.

### Aggregating — like SQL's GROUP BY
```python
df.groupby("city")["score"].mean()     # average score per city
df["score"].sum()                       # total of a column
df.sort_values("score", ascending=False)   # sort rows by a column
```

### Adding/modifying columns
```python
df["passed"] = df["score"] > 60          # new boolean column
df["score_doubled"] = df["score"] * 2     # new numeric column
```

### Writing back to CSV
```python
df.to_csv("output.csv", index=False)     # index=False avoids writing row numbers as a column
```

---

## Today's Tasks

1. **NumPy practice** in `numpy_practice.py`:
   - Create an array of the numbers `[3, 12, 7, 45, 9, 22, 8, 14]` using `np.array`.
   - Print the `sum`, `mean`, `max`, and `min` of the array.
   - Create a new array containing only values greater than 10 (using boolean filtering, not a loop).
   - Create a new array where every value is doubled (using vectorized multiplication, not a loop).

2. **Pandas practice** in `pandas_practice.py`:
   - Load `score.csv` (from Day 3) using `pd.read_csv()`.
   - Print `df.head()` and `df.describe()`.
   - Filter and print only the rows where `score > 80`.
   - Add a new column `grade` where score `>= 90` → `"A"`, `>= 75` → `"B"`, else `"C"` (hint: you can use a list comprehension combined with `df["grade"] = [...]`, or look up `pd.cut`/`apply` if you want a preview of tomorrow's territory — either is fine for today).
   - Group by `city` (if present in your CSV) and print the average score per city. If your `score.csv` doesn't have a city column, add one manually for this exercise.
   - Save the updated DataFrame (with the new `grade` column) to `updated_scores.csv` using `to_csv`.

3. **Compare mentally**: Write one sentence (as a comment in your file) comparing how you'd filter "scores greater than 80" using: (a) a plain Python loop, (b) a list comprehension, (c) pandas boolean filtering. This is just to lock in when each style is the natural choice.

**Time estimate:** 2 hours total (this is a denser day than 1–3, since it introduces two new libraries).

---

**Tomorrow (Day 5 preview):** Working with missing data, merging/joining DataFrames (like SQL joins), and a first look at `matplotlib`/`seaborn` for basic data visualization — the last stretch of "core data handling" before moving into actual model training.