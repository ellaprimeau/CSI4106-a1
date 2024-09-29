import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

url = 'https://raw.githubusercontent.com/ellaprimeau/CSI4106-a1/refs/heads/master/WineQT.csv'
data = pd.read_csv(url, encoding='latin1')

hist = data.hist()
plt.show()