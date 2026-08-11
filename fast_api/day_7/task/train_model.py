from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load the built-in iris dataset (150 rows, 4 features, 3 classes)
X, y = load_iris(return_X_y=True)

# Train a simple classifier — no tuning needed, this is just to get a model artifact
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save it next to this script, regardless of where you run the script from
MODEL_PATH = Path(__file__).parent / "model.pkl"
joblib.dump(model, MODEL_PATH)

print(f"Model saved to {MODEL_PATH}")