""" 
    MSSV : 19516521
    Họ và tên : Trần Anh Vũ
 """

from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

mu = 4.7
sigma = 0.47
""" Câu 1 """
a = norm.cdf((4.4-mu)/sigma)
print('Xác suất chọn một bạn được coi là lùn (nhỏ hơn 164cm) :',a)

""" Câu 2  """
b = 1 - norm.cdf((180-mu)/sigma)
print('Xác suất chọn một bạn được coi là cao lớn (lớn hơn 180cm) :',b)

""" Câu 3 """
c = norm.cdf((178-mu)/sigma) - norm.cdf((168-mu)/sigma)
print('Xác suất chọn một bạn trong khoảng 168cm - 178cm :',c)

""" Câu 4 """
d = norm.ppf(0.06,mu,sigma)
print('Vậy thấp bé là : ',d)

""" Câu 5 """
e = norm.ppf(0.94,mu,sigma)
print('Vậy cao lớn là : ',e)

""" Câu 6  """
chuan = np. arange(-10,10,0.25)

pdf = norm.pdf(chuan)
PDF = plt.plot(chuan, pdf)
plt.xlabel('X')
plt.ylabel('P_X(X)')
plt.show()

chuan = np.arange(-10,10,0.25)
cdf = norm.cdf(chuan)
CDF=plt.plot(chuan, cdf)
plt.xlabel('x')
plt.ylabel('P_X(x)')
plt.show()