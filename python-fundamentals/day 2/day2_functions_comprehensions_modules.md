# Day 2 — Python Fundamentals (Java → Python)
**Topics:** Functions, List/Dict Comprehensions, Modules & Imports

---

## 1. Functions — No return type, no access modifiers

Java forces you to declare a return type and often wraps functions inside a class. Python functions are standalone and untyped by default.

```java
// Java
public int add(int a, int b) {
    return a + b;
}
```

```python
# Python
def add(a, b):
    return a + b
```

Key differences:
- `def` replaces the return type + method name.
- No `public`/`private` — Python uses naming convention instead: `_name` means "internal use", not enforced by the compiler.
- No overloading — a function name can only point to one definition at a time (last one wins).

**Default arguments** (like Java's overloaded methods, but simpler):
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Anubhav")                # Hello, Anubhav!
greet("Anubhav", "Namaste")      # Namaste, Anubhav!
```

**Keyword arguments** — pass by name, order doesn't matter:
```python
greet(greeting="Hi", name="Anubhav")
```

**Variable-length arguments** (Java's varargs equivalent):
```python
def total(*numbers):        # like Java's int... numbers
    return sum(numbers)

total(1, 2, 3, 4)   # 10
```

**Type hints for functions** (recommended — closest to Java's explicitness):
```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## 2. List & Dict Comprehensions — Python's answer to Streams

If you've used Java Streams (`list.stream().filter(...).map(...)`), comprehensions are Python's more compact version of the same idea.

```java
// Java - squares of even numbers
List<Integer> result = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList());
```

```python
# Python - same logic
result = [n * n for n in numbers if n % 2 == 0]
```

Read it as: **"n squared, for each n in numbers, if n is even."**

More examples:
```python
# List comprehension - basic
squares = [n * n for n in range(10)]

# List comprehension - with condition
evens = [n for n in range(20) if n % 2 == 0]

# Dict comprehension - like Java's Collectors.toMap()
square_map = {n: n * n for n in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "yo"]}
```

Why this matters for MLOps: you'll use comprehensions constantly when cleaning/transforming data (filtering rows, building lookup dicts, extracting columns) before you ever touch pandas.

---

## 3. Modules & Imports — Python's package system

Java's `import` pulls in a class from a package. Python's `import` pulls in a **module** (a `.py` file) or **package** (a folder of modules).

```java
// Java
import java.util.List;
import java.util.ArrayList;
```

```python
# Python
import math
from math import sqrt
import numpy as np          # common alias convention
from collections import Counter
```

Import styles:
| Style | Example | When to use |
|---|---|---|
| `import module` | `import math` | Access via `math.sqrt()` |
| `from module import name` | `from math import sqrt` | Direct access via `sqrt()` |
| `import module as alias` | `import numpy as np` | Standard convention for common libs |
| `from module import *` | ❌ avoid | Pollutes namespace, avoid in real code |

**Your own modules**: any `.py` file can be imported by another.
```python
# utils.py
def square(n):
    return n * n
```
```python
# main.py
import utils
print(utils.square(5))   # 25

# or
from utils import square
print(square(5))
```

There's no `public class Main { public static void main(...) }` boilerplate — a Python file just runs top to bottom when executed. The common convention to mark "this is the entry point" is:
```python
if __name__ == "__main__":
    main()
```
This means: "only run this block if the file is executed directly, not when imported elsewhere." You'll see this in almost every serious Python project.

---

## Today's Tasks

1. **Write 3 functions** in a file `functions.py`:
   - `is_even(n)` → returns `True`/`False`
   - `factorial(n)` → returns factorial using a loop (not recursion yet)
   - `greet(name, greeting="Hello")` → uses a default argument
   - Add type hints to all three (`def is_even(n: int) -> bool:`)

2. **Comprehension practice** in `comprehensions.py`:
   - Given `numbers = [3, 12, 7, 45, 9, 22, 8, 14]`, use a list comprehension to build a list of only the even numbers.
   - Use a dict comprehension to build `{number: "Even"/"Odd"}` for every number in the list.
   - Use a list comprehension to get the **square** of every number greater than 10.

3. **Modules practice**:
   - Create `utils.py` containing your `is_even` and `factorial` functions from task 1.
   - Create `main.py` that imports from `utils.py` and calls both functions.
   - Add the `if __name__ == "__main__":` guard in `main.py`.

4. **Rewrite a Java habit in Python**: Take a Java method that used a `for` loop to build a filtered list (something you've likely written many times, like filtering a list of objects by a condition) and rewrite it as a one-line Python comprehension.

**Time estimate:** 1.5–2 hours total.

---

**Tomorrow (Day 2 preview... wait, Day 3 preview):** Exception handling, file I/O (reading/writing CSV and JSON — the format you'll use constantly for ML datasets and configs), and an intro to virtual environments (`venv`) — Python's answer to Java's per-project dependency isolation.
