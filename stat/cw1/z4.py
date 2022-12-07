import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv('brain_size.csv', sep=';', na_values=".")

data_pogrupowane = data.groupby('Gender')
for gender, value in data_pogrupowane['VIQ']: 
    print((gender,value.mean()))

scatter_matrix(data[['VIQ','PIQ','FSIQ']])
plt.show()