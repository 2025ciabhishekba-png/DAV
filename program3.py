import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\user\Downloads\archive (5)\Iris.csv")

print("First 5 rows of the database:")
print(df.head())
print("last 5 rows of the database:")
print(df.tail())
print("\n shape of the database:")
print(df.shape)
print("\n column names:")
print(df.columns)
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.duplicated().sum())
plt.figure(figsize=(8,5))
sns.histplot(data=df,x="SepalLengthCm",bins=10)
plt.title("Distribution os Sepal length")
plt.xlabel("sepal Length (cm)")
plt.ylabel("number of flowers")
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="Species",y="SepalLengthCm")
plt.title("Sepal length by Species")
plt.xlabel("species")
plt.ylabel("Sepal length (cm)")
plt.show()
plt.figure(figsize=(8,5))
sns.scatterplot(data=df,x="SepalLengthCm",y="PetalLengthCm",hue="Species")
plt.title("Sepal length vs Petal length")
plt.xlabel("Sepal length (cm)")
plt.ylabel("Petal length (cm)")
plt.show()
numeric_columns=[
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]
correlation = df[numeric_columns].corr()
print(correlation)
plt.figure(figsize=(8,5))
sns.heatmap(correlation,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
