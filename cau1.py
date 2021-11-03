import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats_basic import skew
from scipy.stats.stats import kurtosis
import statsmodels.api as smi

path = 'csv_Data_BMI.csv'
data = pd.read_csv(path)
data.info()
df_weight_nam = pd.DataFrame(data,columns=['Weight_kg','Gender']).query('Gender== "Male"')
df_weight_nu = pd.DataFrame(data,columns=['Weight_kg','Gender']).query('Gender== "Female"')
print(df_weight_nam.head())


""" Thống kê mô tả """
weight_kg_nam = np.array(df_weight_nam['Weight_kg'])
weight_kg_nu = np.array(df_weight_nu['Weight_kg'])