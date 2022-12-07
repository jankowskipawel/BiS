import numpy as np
import pandas as pd
import statistics
import scipy.stats as scp


data2 = np.loadtxt("Wzrost.csv",delimiter=',')
print("kurtosis: ",scp.kurtosis(data2))
print("skewness: ",scp.skew(data2))
print("describe: ",scp.describe(data2))
