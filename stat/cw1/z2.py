import numpy as np
import pandas as pd
import statistics

data2 = np.loadtxt("Wzrost.csv",delimiter=',')
print("median high: ",statistics.median_high(data2))
print("median low: ",statistics.median_low(data2))
print("mode: ",statistics.mode(data2))
print("pvariance: ",statistics.pvariance(data2))
print("variance: ",statistics.variance(data2))
print("pstdev: ",statistics.pstdev(data2))
print("stdev: ",statistics.stdev(data2))