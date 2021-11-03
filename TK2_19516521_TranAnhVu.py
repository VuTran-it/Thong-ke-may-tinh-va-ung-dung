""" 
    MSSV : 19516521
    Họ và tên : Trần Anh Vũ
 """

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew

X = [15,18,21,20,20,19,22,24,18,17,18,18,19,45,65]

print('Kurtosis la : ' + str(kurtosis(X,fisher=False)))
print('Skew la : ' + str(skew(X)))
print('Min la : ' +str (np.min(X)))
print('Max la : ' +str (np.max(X)))
print('Trung binh là :' + str(np.mean(X)))
print('Sdt la :' + str(np.std(X)))
print('Var la ' + str(np.var(X)))
print('Media la : ' + str(np.median(X)))
print('Q25%:' +str(np.percentile(X,25)))
print('Q50%:' +str(np.percentile(X,50)))
print('Q75%:' +str(np.percentile(X,75)))
q75,q25 = np.percentile(X,[75,25])
iqr = q75 - q25 
print('IQR = ' +str(iqr))
LL = q25 - 1.5*iqr
UL = q75 + 1.5*iqr
print('LL = ' + str(LL))
print('UL = ' + str(UL))


plt.boxplot(X,sym='*')
plt.ylabel('Độ tuổi')
plt.title('Độ tuổi sinh viên năm nhất')
plt.show()

plt.hist(X, bins= 5)
plt.title('Histogram Độ tuổi sinh viên năm nhất')
plt.xlabel('Độ tuổi')
plt.show()