from ast import Str
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats_basic import skew
from scipy.stats.stats import kurtosis
import statsmodels.api as smi

""" a """
path = 'Data_Bicycle_Counter.csv'
data = pd.read_csv(path)


data_500 = data.head(500)
print(data_500)
""" b """
Bridge_Total = pd.DataFrame(data.head(500),columns=['Date','Fremont Bridge Total'])
Fremont_Total = np.int64(np.array(Bridge_Total['Fremont Bridge Total']))
