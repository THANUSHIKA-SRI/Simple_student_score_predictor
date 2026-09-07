import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
# 1. Load the dataset
data = pd.read_csv("data/students.csv")
# 2. Select input features
X = data[["hours_studied", "attendance"]]
# 3. Select target
y = data["score"]
model = LinearRegression()
model.fit(X, y)
#save the trained model
joblib.dump(model, "model/student_score_model.pkl")
print("Model trained and saved as student_score_model.pkl")