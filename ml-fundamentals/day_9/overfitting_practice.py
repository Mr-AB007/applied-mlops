from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X,Y = load_iris(return_X_y=True)
X_train_a, X_test_a, y_train_a, y_test_a = train_test_split(
    X, Y, test_size=0.02, random_state=42
)

model_a = LogisticRegression(max_iter=200)
model_a.fit(X_train_a, y_train_a)

print("Experiment A (test_size=0.02)")
print(f"  Train accuracy: {model_a.score(X_train_a, y_train_a):.3f}")
print(f"  Test accuracy:  {model_a.score(X_test_a, y_test_a):.3f}")


# --- Experiment B: normal 80/20 split, but an unconstrained decision tree ---
X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model_b = DecisionTreeClassifier()
model_b.fit(X_train_b, y_train_b)
print(f"Experiment B (test_size=0.2)")
print(f"  Train accuracy: {model_b.score(X_train_b, y_train_b):.3f}")
print(f"  Test accuracy:  {model_b.score(X_test_b, y_test_b):.3f}")