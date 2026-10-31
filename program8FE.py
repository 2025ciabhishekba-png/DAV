import pandas as pd
import numpy as np
data = {
    'Study_Hours': [2, 4, 6, 8, 10, 3, 5, 7, 9, 12],
    'Attendance': [60, 65, 70, 75, 80, 62, 68, 78, 85, 95],
    'Assignment_Score': [40, 50, 55, 65, 70, 45, 60, 72, 80, 90],
    'Exam_Score': [45, 50, 60, 65, 75, 48, 58, 70, 82, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\nStatistical Summary:")
print(df.describe())
from sklearn.preprocessing import MinMaxScaler

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Apply normalization
normalized_data = scaler.fit_transform(df)

# Convert into DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("Normalized Dataset:")
print(normalized_df.round(2))

# Verify minimum and maximum
print("\nMinimum values:")
print(normalized_df.min())

print("\nMaximum values:")
print(normalized_df.max())
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Apply standardization
standardized_data = scaler.fit_transform(df)

# Convert into DataFrame
standardized_df = pd.DataFrame(
    standardized_data,
    columns=df.columns
)

print("Standardized Dataset:")
print(standardized_df.round(2))

# Verify mean and standard deviation
print("\nMean of each feature:")
print(standardized_df.mean().round(2))

print("\nStandard deviation of each feature:")
print(standardized_df.std(ddof=0).round(2))
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
