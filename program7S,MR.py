import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "Assignment_Marks": [10, 12, 15, 16, 18, 20, 22, 24, 26, 28],
    "Marks": [35, 40, 45, 50, 55, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
X_simple = df[["Study_Hours"]]

X_multiple = df[["Study_Hours", "Attendance", "Assignment_Marks"]]

y = df["Marks"]
X_train_s, X_test_s, y_train, y_test = train_test_split(X_simple, y, test_size=0.2, random_state=42)

X_train_m, X_test_m, _, _ = train_test_split(X_multiple, y, test_size=0.2, random_state=42)
