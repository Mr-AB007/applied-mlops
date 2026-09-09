# Day 9 — ML Fundamentals: Train/Test Split, Overfitting, Evaluation (Java → Python)
**Topics:** train/test split, what overfitting actually is, accuracy/precision/recall/confusion matrix

This is the first day that's genuinely *new* territory — not a Python-syntax-for-Java-devs translation, but an ML concept with no backend equivalent. Take it slower than usual. Everything here plugs directly into the `train_model.py` stub you've been treating as a black box since Day 7 — today you stop treating it as scaffolding and start understanding what it actually does.

> **Scaffolding vs. learning code:** there's no scaffolding today. Every line below is something you're expected to understand, not just run.

---

## 1. The core problem: how do you know if a model is actually good?

In backend work, "does it work" usually means "does it produce the correct output for a given input" — deterministic, testable with a fixed assertion. ML models don't have a single correct answer to check against in the same way; they generalize from examples, and the real question is: **will it work on data it's never seen?**

This is the entire reason train/test split exists.

## 2. Train/test split

If you train a model on 100% of your data, then check "how well does it do on that same data," you're not testing anything — you're checking whether it *memorized* the answers. That's not useful; in production it'll see requests it has never encountered.

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- `test_size=0.2` — hold back 20% of the data, never let the model see it during training.
- `random_state=42` — seeds the shuffle so the split is reproducible. Without it, you'd get a different random split every run, making results impossible to compare across attempts — the ML equivalent of a flaky test that passes/fails non-deterministically.
- You train on `X_train`/`y_train` only, then evaluate on `X_test`/`y_test` — data the model has never touched.

**Analogy that actually holds up:** it's like a held-out validation set of test cases you never show a candidate during a take-home — if they only do well on the examples they had access to beforehand, that tells you nothing about how they'll perform on a novel problem.

## 3. Overfitting — memorizing instead of generalizing

**Overfitting**: the model performs great on training data, but poorly on test data. It has essentially memorized noise/specifics of the training set rather than learning the general pattern.

**Underfitting**: the model performs poorly on *both* — it hasn't learned enough of the pattern at all (too simple a model, or not enough training).

| | Train accuracy | Test accuracy | Diagnosis |
|---|---|---|---|
| Good fit | 95% | 93% | Generalizes well — small, expected gap |
| Overfit | 99% | 71% | Memorized training data, fails on new data |
| Underfit | 65% | 63% | Model too simple / undertrained for the pattern |

There's no exact Java/backend equivalent, but the closest intuition: it's like a service that passes 100% of its own unit tests (which it was tuned against) but fails constantly in production against real traffic patterns the tests never modeled. The tests looked perfect; they just weren't representative.

You won't fully diagnose or fix overfitting today — that's a deeper topic (regularization, more data, cross-validation) for later. Today's goal is just: **recognize it by comparing train vs. test scores**, nothing more.

## 4. Evaluation metrics — beyond "percent correct"

`accuracy` = correct predictions / total predictions. Simple, but can be **misleading** on imbalanced data.

**Concrete example:** imagine a fraud-detection model where 99% of transactions are legitimate. A model that *always* predicts "not fraud" gets 99% accuracy — while catching zero actual fraud. Accuracy alone hides this completely.

This is why **precision** and **recall** exist:

| Metric | Question it answers | Formula (informal) |
|---|---|---|
| **Precision** | Of everything I flagged as fraud, how much was actually fraud? | TP / (TP + FP) |
| **Recall** | Of all the actual fraud, how much did I catch? | TP / (TP + FN) |

- High precision, low recall → cautious model, misses a lot of real cases but rarely wrong when it does flag something.
- High recall, low precision → aggressive model, catches most real cases but with a lot of false alarms.
- There's almost always a trade-off — you tune toward one or the other based on what a false positive vs. false negative *costs* in your actual use case (a missed fraud case vs. annoying a legitimate customer are very different costs).

### Confusion matrix — the full picture in one table

```python
from sklearn.metrics import confusion_matrix, classification_report

y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

`confusion_matrix` gives you a grid of actual-vs-predicted counts — every metric above is derived from this one table. `classification_report` computes precision/recall/F1 for you per class, so for today you mostly just need to be able to *read* the output, not compute it by hand.

---

## Today's Tasks

Folder: `applied-mlops/ml-fundamentals/day_9/`

1. **`train_test_practice.py`:**
   - Load iris, do a `train_test_split` with `test_size=0.2`, `random_state=42`.
   - Train a `LogisticRegression` on the training set only.
   - Print the model's accuracy on `X_train`/`y_train` AND separately on `X_test`/`y_test` (use `model.score(X, y)`).
   - Write a one-line comment: are these two numbers close together or far apart? What would it mean if the training accuracy were 99% and test accuracy were 60%?

2. **`evaluation_practice.py`:**
   - Using the same train/test split, generate predictions on the test set.
   - Print `confusion_matrix(y_test, y_pred)` and `classification_report(y_test, y_pred)`.
   - In a comment, identify: which class (if any) had the lowest precision or recall? (Iris is a fairly "easy" dataset — don't be surprised if all three classes score well; the goal is reading the report, not finding a dramatic result.)

3. **Deliberately overfit, to see it happen:**
   - Retrain using `test_size=0.02` (almost no held-out data) and compare train vs. test accuracy again.
   - Then try training a `DecisionTreeClassifier` with no depth limit (`DecisionTreeClassifier()` — default has no `max_depth`) instead of `LogisticRegression`, using your normal 80/20 split. Compare train vs. test accuracy for this one too.
   - One-sentence comment: which of these two experiments showed a bigger train/test gap, and does that match what Section 3 predicted?

**Time estimate:** 2–2.5 hours. This is a conceptually denser day than 6–8 — it's fine if it takes longer. Don't rush past the confusion matrix output without actually reading what each number means.

---

**Next up (Day 10):** Feature engineering basics (scaling, encoding categorical variables) using your `census-income-prediction` project's actual dataset for the first time — this is where the roadmap's anchoring project properly kicks off.