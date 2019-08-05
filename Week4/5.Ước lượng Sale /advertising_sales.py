import pandas as pd

# Import dữ liệu
dataframe = pd.read_csv('advertising.csv')

x = dataframe.values[:,1:3]
print(x)
