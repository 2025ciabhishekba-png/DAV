import numpy as np
import pandas as pd

arr = np.array([10,20,30,40,50])
print("Array:", arr)
print("mean:",arr.mean())
print("Reshaped 2D:\n",arr.reshape(5,1))
print("Sliced (index 1 to 3):", arr[1:4])

data = {"Name":['Asha','Ravi','Meera','Karan'],
        "Marks":[88,72,91,65],
        "Branch":['CSE','ECE','CSE','ISE']}
df = pd.DataFrame(data)
print(df)

print("first 2 rows:\n",df.iloc[0:2])
print("Marks column:\n",df[['Name','Marks']])
print("Rows where Marks >70:\n",df[df['Marks']>70])
