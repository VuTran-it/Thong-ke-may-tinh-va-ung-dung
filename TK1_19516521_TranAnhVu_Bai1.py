""" 
    MSSV : 19516521
    Họ và tên : Trần Anh Vũ
 """
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

X = stats.binom(60, 0.25)
nhi_thuc=np.arange(0,60)
pmf = X.pmf(nhi_thuc)

print('Xác suất số lượng trên 40 câu : ', (1-X.cdf(39)))
print ('kỳ vọng : ', X.mean())
print('Phương sai : ', X.var())
print ('Độ lệch chuẩn : ', X.std() )

import seaborn as sns
PMF=sns.barplot(nhi_thuc, pmf)
PMF.set(xlabel='so lan A xay ra ', ylabel='P_X(x)')
plt.show()

cdf=X.cdf(nhi_thuc)
CDF=sns.barplot(nhi_thuc, cdf)
CDF.set(xlabel='so lan A xay ra', ylabel='F_X(x)')
plt.show()