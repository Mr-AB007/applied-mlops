# Day 1 — Python Fundamentals (Java → Python)
**Topics:** Syntax, Variables, Data Types, Control Flow

Since you're coming from 5 years of Java, the fastest path is to map what you already know onto Python's way of doing it. Java is explicit and compiled; Python is dynamic and interpreted. That single difference explains almost every syntax change below.

---

## 1. Syntax — No braces, no semicolons

Java uses `{ }` and `;` to define structure. Python uses **indentation** — it's not a style choice, it's the syntax.

```java
// Java
if (x > 5) {
    System.out.println("big");
}
```

```python
# Python
if x > 5:
    print("big")
```

Key rules:
- A colon `:` starts a new block (`if`, `for`, `while`, `def`, `class`).
- Everything inside the block must be indented the same amount (use 4 spaces — never tabs).
- No semicolons needed (allowed but never used).
- No curly braces, ever.

---

## 2. Variables — No type declarations

Java requires you to declare a type. Python infers it at runtime.

```java
// Java
int age = 30;
String name = "Alex";
```

```python
# Python
age = 30
name = "Alex"
```

This is called **dynamic typing**: the variable itself has no fixed type — the *value* does. You can even reassign a variable to a different type (not recommended, but legal):

```python
x = 5        # x is an int
x = "hello"  # now x is a str — Python allows this
```

**Type hints** (optional, but good practice — closest thing to Java's explicitness):
```python
age: int = 30
name: str = "Alex"
```
In ML/MLOps code, you'll see type hints a lot (FastAPI, Pydantic, etc.), so start using them now.

---

## 3. Data Types

| Java | Python | Notes |
|---|---|---|
| `int`, `long` | `int` | Python `int` has no size limit (no overflow) |
| `double`, `float` | `float` | Always double-precision |
| `boolean` | `bool` | Values are `True`/`False` (capitalized!) |
| `String` | `str` | Immutable, same as Java |
| `char` | *(no separate type)* | A single character is just a `str` of length 1 |
| `ArrayList<T>` | `list` | Dynamic, mutable, no generics needed |
| `HashMap<K,V>` | `dict` | `{"key": "value"}` |
| `HashSet<T>` | `set` | `{1, 2, 3}` |
| N/A | `tuple` | Immutable list — `(1, 2, 3)`. No direct Java equivalent. |

```python
age = 30                  # int
price = 19.99              # float
name = "Alex"               # str
is_active = True            # bool
skills = ["python", "docker", "kubernetes"]   # list (like ArrayList)
info = {"role": "dev", "years": 5}            # dict (like HashMap)
coords = (10.5, 20.3)        # tuple (immutable)
unique_tags = {"ml", "ops", "ml"}  # set -> auto-dedupes to {"ml", "ops"}
```

Check a type anytime with `type(x)`.

---

## 4. Control Flow

### if / elif / else
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```
(`elif` = Java's `else if`, just one word.)

### for loops — iterate over things, not counters
Java's classic `for (int i=0; i<n; i++)` is rare in Python. Instead:

```python
# Loop over a list directly
for skill in skills:
    print(skill)

# Loop with an index (like Java's counting loop)
for i in range(5):       # 0,1,2,3,4
    print(i)

# Loop with both index and value
for i, skill in enumerate(skills):
    print(i, skill)
```

### while loops — same idea as Java
```python
count = 0
while count < 5:
    print(count)
    count += 1   # note: no ++ operator in Python!
```

### Key gotchas coming from Java
- No `++` or `--`. Use `count += 1`.
- `==` compares values (like Java's `.equals()`), not references.
- Booleans are `True` / `False` (capital first letter).
- `and`, `or`, `not` instead of `&&`, `||`, `!`.
- No `switch` statement in classic Python — use `if/elif` or the newer `match` (Python 3.10+):
```python
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case _:
        print("Other")
```

---

## Today's Tasks

1. **Set up your environment**: Install Python 3.11+, and set up VS Code (or PyCharm, since you know JetBrains tools from Java). Confirm with `python3 --version`.
2. **Write a script** `basics.py` that:
   - Declares variables of each type: `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`.
   - Prints each variable along with its type using `type()`.
3. **Control flow practice**:
   - Write a function-free script that loops through a list of numbers `[3, 12, 7, 45, 9, 22]` and prints whether each is even/odd and whether it's greater than 10 — using `if/elif/else` and a `for` loop.
4. **Rewrite a Java habit in Python**: Take any simple Java method you've written before (e.g., FizzBuzz) and re-implement it in Python. This forces you to actively translate syntax rather than just read about it.
5. **Stretch task**: Use `range()` and a `while` loop to print the Fibonacci sequence up to 100.

**Time estimate:** 1.5–2 hours total.

---

**Tomorrow (Day 2 preview):** Functions, lists/dict comprehensions, and Python's import/module system — the pieces you'll lean on constantly once you get into pandas/numpy for ML data work.
