
""" 
    MSSV : 19516521
    Họ và tên : Trần Anh Vũ
 """
""" câu 1 """
# A : bị bệnh 
# B : dương tính
PrA = 8/500000
PrAc = (500000-8)/500000
PrB_A =  0.55
PrB_Ac = 0.45
# Cần tính PrA_B
PrA_B = (PrB_A * PrA) / (PrB_A*PrA + PrB_Ac*PrAc)

print ("Xác xuất người đó nhiễm Covid là : ",PrA_B)


""" Câu 2 :  """
from pandas.core.frame import DataFrame
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

X = stats.binom(60, 0.25)
nhi_thuc=np.arange(0,60)
pmf = X.pmf(nhi_thuc)

print ('kỳ vọng : ', X.mean())
print('Phương sai : ', X.var())
print ('Độ lệch chuẩn : ', X.std() )

print('Xác suất thí sinh đỗ trên 40 câu : ', (1-X.cdf(39)))

import seaborn as sns
PMF=sns.barplot(nhi_thuc, pmf)
PMF.set(xlabel='so lan A xay ra ', ylabel='P_X(x)')
plt.show()

cdf=X.cdf(nhi_thuc)
CDF=sns.barplot(nhi_thuc, cdf)
CDF.set(xlabel='so lan A xay ra', ylabel='F_X(x)')
plt.show()

""" Câu 3 :  """
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np 
mu = 168
sigma = 5 
""" 1. xác suất gọi là lùn (<164cm)"""
a = norm.cdf((164-mu)/sigma)
print('Xác suất chọn một bạn được coi là lùn (nhỏ hơn 164cm) :',a)
""" 2. xác suất gọi là cao (>180cm) """
b = 1 - norm.cdf((180-mu)/sigma)
print('Xác suất chọn một bạn được coi là cao lớn (lớn hơn 180cm) :',b)
""" 3. xác suất trong khoảng 168cm - 178cm """
c = norm.cdf((178-mu)/sigma) - norm.cdf((168-mu)/sigma)
print('Xác suất chọn một bạn trong khoảng 168cm - 178cm :',c)
""" 4.Biết 6% là thấp bé """
d = norm.ppf(0.06,mu,sigma)
print('Vậy thấp bé là : ',d)
""" 5.Chỉ quan tâm đến 6% cao lớn """
e = norm.ppf(0.94,mu,sigma)
print('Vậy cao lớn là : ',e)

""" 6.vẽ biểu đồ """
chuan = np. arange(-10,10,0.25)
pdf = norm.pdf(chuan)
PDF = plt.plot(chuan, pdf)
plt.xlabel('X')
plt.ylabel('P_X(X)')
plt.show()

cdf = norm.cdf(chuan)
CDF=plt.plot(chuan, cdf)
plt.xlabel('x')
plt.ylabel('P_X(x)')
plt.show()

""" Câu 4 :  """
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

print('Kurtosis la : ' + str(kurtosis(weight_kg_nam,fisher=True)))
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