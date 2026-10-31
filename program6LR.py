import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 2, 3,
                      5, 6, 7, 8, 9, 1, 4, 6, 8, 9],
    'Pass': [0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
             1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)

print("Dataset:")
print(df)
X = df[['Hours_Studied']]
y = df['Pass']

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)
print("\nPrecision:", precision_score(y_test, y_pred,
                                      zero_division=0))
print("Recall:", recall_score(y_test, y_pred,
                              zero_division=0))
print("F1-Score:", f1_score(y_test, y_pred,
                            zero_division=0))
