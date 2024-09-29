import pandas as pd
import numpy as np

data = pd.read_csv('train.csv', encoding='latin1')
print(data.isnull().any())
# print(data[data.isnull().any(axis=1)])

