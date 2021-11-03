# MSSV : 19516521
# Họ và Tên : Trần Anh Vũ

""" Cau 1 """
#A:Bị bệnh
#B:dương tính

PrA = 8/500000
PrAc = (500000-8)/500000
PrB_A = 0.55
PrB_Ac = 0.45 
#Cần tính là PrA_B
PrA_B = (PrB_A*PrA)/(PrB_A*PrA + PrB_A*PrAc)

print('h xác suất một người B ở thành phố A bị nhiễm Covid-19 : ',PrA_B)

""" Câu 2 : """
from numpy.lib.function_base import digitize
from scipy.stats import norm 
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt 

mu = 168
sigma = 4 
""" a """
a = norm.cdf((160-mu)/sigma)
print('Xác suất được coi là lun <160cm : ',a)

""" b """

b = 1 - norm.cdf((176-mu)/sigma)
print('Xác suất được coi là cao >176cm : ',b)

""" c """
c =norm.cdf((175-mu)/sigma) - norm.cdf((170-mu)/sigma)
print('Xác suất trong khoản 170-175cm : ',c)

""" d"""
d =norm.ppf(0.04,mu,sigma)
print('Vậy 4% thấp bé là: ',d)

""" e"""
e =norm.ppf(0.88,mu,sigma)
print('Vậy cao lớn là  ',e)

""" f """
x = mu-3*sigma
y = mu+3*sigma
chuan = np.arange(x,y,1)
pdf = norm.pdf(chuan)
PDF = plt.plot(chuan,pdf)
plt.xlabel('X')
plt.ylabel('P_X(x)')
plt.show()

cdf = norm.pdf(chuan)
CDF = plt.plot(chuan,cdf)
plt.xlabel('X')
plt.ylabel('P_X(x)')
plt.show()

""" Cau 3 :  """
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
data.info()
print(data.head(20))

""" b """
Bridge_Total = pd.DataFrame(data.head(500),columns=['Date','Fremont Bridge Total'])
Fremont_Total = np.int64(np.array(Bridge_Total['Fremont Bridge Total']))

print('kurtosis : ' + str(kurtosis(Fremont_Total,fisher=True)))
print('Skew : ' + str(skew(Fremont_Total)))
print('Min la : '+ str(np.min(Fremont_Total)))
print('Max la : '+ str(np.max(Fremont_Total)))
print('Trung binh la : '+ str(np.mean(Fremont_Total)))
print('Std la : '+ str(np.std(Fremont_Total)))
print('Var la : '+ str(np.var(Fremont_Total)))
print('Media la : '+ str(np.median(Fremont_Total)))
print('Q25 la : '+ str(np.percentile(Fremont_Total,25)))
print('Q50 la : '+ str(np.percentile(Fremont_Total,50)))
print('Q75 la : '+ str(np.percentile(Fremont_Total,75)))
q75,q25 = np.percentile(Fremont_Total,[75,25])
iqr = q75 - q25
print('IQR :',iqr)
LL = q25 - 1.5*iqr
UL = q75 +1.5*iqr
print('LL Là :',LL)
print('UL Là :',UL)

plt.hist(Fremont_Total,bins=12)
plt.title("Xe đi 2 chiều")
plt.xlabel('Xe')
plt.show()

plt.boxplot(Fremont_Total,sym='*')
plt.title("Xe đi 2 chiều")
plt.ylabel('Xe')
plt.show()

Bridge_East_Sidewalk = pd.DataFrame(data.head(500),columns=['Date','Fremont Bridge East Sidewalk'])
East_Sidewalk =np.array(Bridge_East_Sidewalk['Fremont Bridge East Sidewalk'])

""" c """
smi.qqplot(East_Sidewalk,line="s")
plt.title('QQ-polt Fremont Bridge East Sidewalk')
plt.show() 

""" d """
Bridge_West_Sidewalk = pd.DataFrame(data.head(500),columns=['Date','FremontBridge West Sidewalk'])
West_Sidewalk =np.array(Bridge_West_Sidewalk['FremontBridge West Sidewalk'])
data_ss = [East_Sidewalk,West_Sidewalk]
fig1,ax1 =plt.subplots()
ax1.set_title('So sanh')
ax1.boxplot(data_ss)
plt.xticks([1,2],['East Sidewalk','West Sidewalk'])

""" e """
plt.scatter(East_Sidewalk,West_Sidewalk)
plt.title('Biểu đồ scatter')
plt.ylabel('East_Sidewalk')
plt.xlabel('West Sidewalk')

