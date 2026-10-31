import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv(r"C:\Users\user\Downloads\archive (6)\melb_data.csv")
print("First five rows of the dataset")
df.head()
 print("\n Shape of Dataset:")
 print(df.shape)
 print("\nColumns names:")
 print(df.columns)
 print("Dataset Information:")
 print(df.info())
 print("Statistical summary:")
 print(df.describe())
print("\nMisssing values before Preprocessing:")
print(df.isnull().sum())
df_mean = df.copy()
mean_building_area = df_mean["BuildingArea"].mean()
df_mean["BuildingArea"]= df_mean["BuildingArea"].fillna(mean_building_area)
print("\nMean Building Area:", mean_building_area)
print("Missing BuildingArea values after Mean Imputation:")
print(df_mean["BuildingArea"].isnull().sum())
df_median = df.copy()
median_year_built = df_median["YearBuilt"].median()
df_median["YearBuilt"]= df_median["YearBuilt"].fillna(median_year_built)
print("\nMedian Year Built:", median_year_built)
print("Missing YearBuilt values after Median Imputation:")
print(df_median["YearBuilt"].isnull().sum())
df_ffill=df.copy()
df_ffill["Car"]=df_ffill["Car"].ffill()
df_ffill["Car"].isnull().sum()




comparision = pd.DataFrame({
    "Original": df["BuildingArea"].head(15),
    "Mean Imputed": df_mean["BuildingArea"].head(15),
    
    "Original":df["YearBuilt"].head(15),
    "Median Imputed": df_median["YearBuilt"].head(15),
    
    "Original":df["Car"].head(15),
    "Forward Filled": df_ffill["Car"].head(15),
})

print("\nComparision of Imputation Methods:")
print(comparision)
df_processed = df.copy()
council_mode = df_processed["CouncilArea"].mode()[0]
df_processed["CouncilArea"] = df_processed["CouncilArea"].fillna(council_mode)
print("\nCouncilArea Mode:", council_mode)
print("\nMissing Categorical values After Implementation:")
print(df_processed[["CouncilArea"]].isnull().sum())
df_encoded = pd.get_dummies(
        df_processed,
columns= ["Type", "Method"],
dtype= int
)
print("\nDataset After One-Hot Encoding:")
print(df_encoded.head())
df_label = df.copy()
label_encoder = LabelEncoder()

df_label["CouncilArea_Encoded"] = label_encoder.fit_transform(
df_label["CouncilArea"]
)
print("\nLabel Encoding of CouncilArea:")
print(
df_label[
    ["CouncilArea", "CouncilArea_Encoded"]
].head(10)
)

