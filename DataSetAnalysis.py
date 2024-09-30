import pandas as pd
import numpy as np
from sklearn import preprocessing
from matplotlib import pyplot as plt

url = 'https://raw.githubusercontent.com/ellaprimeau/CSI4106-a1/refs/heads/master/WineQT.csv'
data = pd.read_csv(url, encoding='latin1')

# data['chlorides'].hist()
# plt.show()

plt.hist(preprocessing.quantile_transform(data[['chlorides']], output_distribution="normal"))
plt.show()
# plt.plot(preprocessing.quantile_transform(data['chlorides']))
# plt.show()
