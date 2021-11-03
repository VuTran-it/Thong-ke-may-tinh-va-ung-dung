import numpy as np 
diem = np.random.randint(0,11,100)
bien_ngau_nhien, tan_so = np.unique(diem,return_counts=True)
pmf = tan_so/100
print( np.column_stack((bien_ngau_nhien,pmf)))

import matplotlib.pyplot as plt
import seaborn as sns 
PMF = sns.barplot(bien_ngau_nhien,pmf)
PMF.set(xlabel='Diem',ylabel = 'P_(X)')
plt.show()

for i in range(0,11):
    cdf = pmf
    cdf[i] = cdf[i-1] + pmf[i]
              
CDF = sns.barplot(bien_ngau_nhien,cdf)
CDF.set(xlabel='Diem',ylabel='F_X(X)')
plt.show()