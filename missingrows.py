import pandas as pd

data = {
    "name": ['ram', 'sam', 'sayan', 'ghosh'],
    "age": [15, 24, 20, None],
    "salary": [30000, None, 40000, 50000]
}

rf = pd.DataFrame(data)
print("Original DataFrame:")
print(rf)

# Missing rows values search
print(rf.isnull().sum())

# Drop missing rows values
print(rf.dropna())
