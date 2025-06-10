import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

from preprocess import preprocess_dataframe, extract_tfidf_features

# Load data
df = pd.read_csv("data/papers.csv")

# Preprocess text
df = preprocess_dataframe(df)

# TF-IDF on title and abstract
tfidf_title, _ = extract_tfidf_features(df["clean_title"], max_features=300)
tfidf_abstract, _ = extract_tfidf_features(df["clean_abstract"], max_features=1000)

# Combine features
from scipy.sparse import hstack
X = hstack([tfidf_title, tfidf_abstract])

# Target
y = df["citations"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
rmse = mean_squared_error(y_test, preds, squared=False)
print(f"Test RMSE: {rmse:.2f}")

# Save model
joblib.dump(model, "models/xgb_model.pkl")
