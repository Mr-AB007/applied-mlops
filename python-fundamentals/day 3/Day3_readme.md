# Day 3 — Python Fundamentals (Java → Python)
**Topics:** Exception Handling, File I/O (CSV & JSON), Virtual Environments

---

## 1. Exception Handling — try/except instead of try/catch

Same concept as Java, different keyword and much looser rules — Python doesn't force you to declare or catch checked exceptions.

```java
// Java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Done");
}
```

```python
# Python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Done")
```

Key differences:
- `except` replaces `catch`.
- No checked vs. unchecked exceptions — **all** exceptions are "unchecked." Nothing forces you to handle anything.
- Catching multiple exception types:
```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That wasn't a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")
```
- Catch-all (like Java's `catch (Exception e)`, but usually discouraged unless you re-raise or log):
```python
except Exception as e:
    print(f"Something went wrong: {e}")
```
- **Raising exceptions** (like Java's `throw`):
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```
- **Custom exceptions** (like Java's custom exception classes):
```python
class InsufficientFundsError(Exception):
    pass

raise InsufficientFundsError("Balance too low")
```

Why this matters for MLOps: almost every pipeline step (reading a file, calling an API, loading a model) can fail at runtime, and production ML code lives or dies by how well it handles those failures instead of crashing silently.

---

## 2. File I/O — Reading/Writing JSON and CSV

This is the part you'll use constantly — ML configs are usually JSON/YAML, and datasets are usually CSV.

### Plain text files
```java
// Java
BufferedReader reader = new BufferedReader(new FileReader("data.txt"));
```

```python
# Python — the "with" block auto-closes the file (like Java's try-with-resources)
with open("data.txt", "r") as f:
    content = f.read()

with open("output.txt", "w") as f:
    f.write("Hello, MLOps!")
```
The `with` statement guarantees the file gets closed even if an error happens inside the block — you never need to call `f.close()` manually.

### JSON (Python's built-in `json` module)
```python
import json

# Writing a dict to a JSON file
config = {"model": "resnet50", "epochs": 10, "lr": 0.001}
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

# Reading a JSON file back into a dict
with open("config.json", "r") as f:
    loaded_config = json.load(f)

print(loaded_config["epochs"])   # 10
```
This is roughly equivalent to Jackson/Gson in Java, but built into the standard library — no extra dependency needed.

### CSV (Python's built-in `csv` module)
```python
import csv

# Writing rows to a CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Anubhav", 92])
    writer.writerow(["Sup", 88])

# Reading rows back
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Reading as dictionaries (very common pattern — like a lightweight row object)
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])
```
Later you'll mostly use `pandas.read_csv()` instead of the raw `csv` module for real datasets — but understanding this built-in version first makes pandas make a lot more sense.

---

## 3. Virtual Environments — Python's per-project dependency isolation

In Java, Maven/Gradle manage per-project dependencies via `pom.xml`/`build.gradle`, and you rarely think about "global" vs "project" libraries. Python doesn't have that built into the language — **you** have to isolate dependencies manually using a **virtual environment (venv)**.

Without a venv, every project on your machine shares the same global Python packages — which breaks fast once two projects need different versions of the same library (e.g., one MLOps tool needs `numpy 1.24`, another needs `numpy 2.0`).

```bash
# Create a virtual environment (creates a "venv" folder)
python3 -m venv venv

# Activate it
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# Your terminal prompt will now show (venv) — confirming it's active

# Install packages — these go into THIS project's venv only
pip install numpy pandas

# See what's installed in this environment
pip freeze

# Save dependencies to a file (like Java's pom.xml, but simpler)
pip freeze > requirements.txt

# Someone else (or future you) can recreate the exact same environment:
pip install -r requirements.txt

# Deactivate when done
deactivate
```

**Important convention**: add `venv/` to your `.gitignore` — you never commit the virtual environment folder itself, only `requirements.txt`. Anyone cloning your repo runs `pip install -r requirements.txt` to rebuild it.

---

## Today's Tasks

1. **Exception handling practice** in `errors.py`:
   - Write a function `safe_divide(a, b)` that returns the division result, but catches `ZeroDivisionError` and returns `None` with a printed message instead of crashing.
   - Write a function `validate_age(age)` that `raise`s a `ValueError` if age is negative, otherwise returns the age.
   - Wrap a call to `validate_age(-5)` in a `try/except` block and print a friendly error message.

2. **JSON practice** in `json_practice.py`:
   - Create a dict representing a model config: `{"model_name": "resnet50", "epochs": 20, "batch_size": 32, "learning_rate": 0.001}`.
   - Write it to `model_config.json` using `json.dump`.
   - Read it back using `json.load` and print just the `learning_rate`.

3. **CSV practice** in `csv_practice.py`:
   - Create a CSV file `scores.csv` with columns `name, score` and at least 4 rows of sample data.
   - Read it back using `csv.DictReader` and print only the rows where `score` (converted to `int`) is greater than 80.

4. **Virtual environment setup**:
   - Inside your `applied-mlops` repo, create a venv: `python3 -m venv venv`.
   - Activate it, run `pip install pandas`, then run `pip freeze > requirements.txt`.
   - Add `venv/` to a `.gitignore` file so it never gets committed.
   - Commit `requirements.txt` and `.gitignore` (not the `venv/` folder itself).


---

