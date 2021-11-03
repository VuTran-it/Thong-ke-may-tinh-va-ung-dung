import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats_basic import skew
from scipy.stats.stats import kurtosis
import statsmodels.api as smi

path = 'Data_Excercise\csv_Data_BMI.csv'
data = pd.read_csv(path)
data.info()
df_weight_nam = pd.DataFrame(data,columns=['Weight_kg','Gender']).query('Gender== "Male"')
df_weight_nu = pd.DataFrame(data,columns=['Weight_kg','Gender']).query('Gender== "Female"')
print(df_weight_nam.head())


""" Thống kê mô tả """
weight_kg_nam = np.array(df_weight_nam['Weight_kg'])
weight_kg_nu = np.array(df_weight_nu['Weight_kg'])
""" 

""" print('Kurtosis la : ' + str(kurtosis(weight_kg_nam,fisher=True)))
print('Skew la : ' + str(skew(weight_kg_nam)))
print('Min la : ' +str (np.min(weight_kg_nam)) + " kg")
print('Max la : ' +str (np.max(weight_kg_nam)) + " kg")
print('Trung binh là :' + str(np.mean(weight_kg_nam)))
print('Sdt la :' + str(np.std(weight_kg_nam)))
print('Var la ' + str(np.var(weight_kg_nam)))
print('Media la : ' + str(np.median(weight_kg_nam)))
print('Q25%:' +str(np.percentile(weight_kg_nam,25)))
print('Q50%:' +str(np.percentile(weight_kg_nam,50)))
print('Q75%:' +str(np.percentile(weight_kg_nam,75)))
q75,q25 = np.percentile(weight_kg_nam,[75,25])
iqr = q75 - q25 
print('IQR = ' +str(iqr))
LL = q25 - 1.5*iqr
UL = q75 + 1.5*iqr
print('LL = ' + str(LL))
print('UL = ' + str(UL))

plt.hist(weight_kg_nam, bins= 5)
plt.title('Cân nặng của nam')
plt.xlabel('KG')
plt.show()

plt.boxplot(weight_kg_nam,sym='*')
plt.ylabel('KG')
plt.title('Cân nặng của nam')
plt.show() 

""" So sánh cân nặng 2 nhóm """
data_weight=[weight_kg_nam,weight_kg_nu]
fig1,ax1=plt.subplots()
ax1.set_title('Boxplot cân nặng giữa nam và nữ')
ax1.boxplot(data_weight)
plt.xticks([1,2],['Cân nặng của Nam','Cân nặng của Nữ'])
plt.show()

""" Phân bố """
smi.qqplot(weight_kg_nam, line = "s")
plt.title('QQ-Plot can nang cua nam')
plt.show()


""" Biểu đồ scatter plot của nam """
df_Height_nam = pd.DataFrame(data,columns=['Height_cm','Gender']).query('Gender== "Male"')
Height_nam = np.array(df_Height_nam['Height_cm'])
colors = np.array(["red","green"])
plt.scatter(weight_kg_nam, Height_nam)
plt.title("Biểu đồ scatter plot của nam")
plt.ylabel("Chiều cao - cm")
plt.xlabel("Cân nặng - kg")
plt.show()