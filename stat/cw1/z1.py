import numpy as np
import pandas as pd
import statistics
from scipy.stats import scoreatpercentile

csv = pd.read_csv('MDR_RR_TB.csv')
data = csv['e_rr_pct_new']
print("max: ",data.min())
print("min: ",data.max())
print("mean: ",data.mean())

data1 = np.loadtxt("MDR_RR_TB.csv", delimiter=',',usecols=(5),unpack=True)

print(data1)
