import pandas as pd
df = pd.read_csv(r"C:\Users\user\Downloads\archive\student_performance.csv")
print("Dataset loaded successfully!")
print("\n First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("Shape of the dataset:")
print(df.shape)
print("Shape of the dataset:")
print(df.shape)
print("\nData types:")
print(df.dtypes)
print("\nDescriptive Stastics:")
print(df.describe())
print("\nStastics including categorical columns:")
print(df.describe(include='all'))
print("\nmissing values in each columns:")
print(df.isnull().sum())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
print("\nNumber of Duplicate student IDs:")
print(df['student_id'].duplicated().sum())
print("\nNumber of students in each grade:")
print(df['grade'].value_counts())
grade_info = pd.DataFrame({
    'grade': ['A','B','c','D','F'],
    'grade_description': [
        'Excellent',
        'Good',
        'Average',
        'Below Average',
        'Fail'
    ]
})

print("\nGrade Information DataFrame:")
print(grade_info)
merged = pd.merge(
df,
grade_info,
on = 'grade',
how = 'left'
)
print("\n Merged DataFrame:")
print(merged.head())
grade_details = pd.DataFrame({
    'description': [
        'Excellent',
        'Good',
        'Average',
        'Below Average',
        'Fail'
    ],
    'perfomance_level': [
        'Very High',
        'High',
        'Medium',
        'Low',
        'Very Low'
    ]
}, index= ['A','B','C','D','F'])
print(grade_details.head())
grade_counts =df['grade'].value_counts().to_frame('student_count')
print(grade_counts.head())
joined = grade_counts.join(grade_details)
print(joined)
df1 =df.iloc[:100]
df2 =df.iloc[100:200]
combined = pd.concat([df1,df2])
print("\nConcatenated DataFrame:")
print(combined.head())
average_score = df.groupby('grade')['total_score'].mean()
print("\n Average Total score by grade:")
print(average_score)
pivot = pd.pivot_table(
df,
values = 'total_score',
index = 'grade',
aggfunc = 'mean')

print("\nPivot Table  = Averge score by Grade:")
print(pivot)
