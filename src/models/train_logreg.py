import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from src.utils.paths import SPY_DIR

df = pd.read_csv(SPY_DIR/"spy_features.csv", parse_dates=["Date"])
X = df.drop(columns=["Date", "target"])
y = df["target"]

split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))