import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st 

# Bài 1 : Gree M&M Candies
path = r'F:\Wed\Python\DataSet\18_M&M.xls'
data = pd.read_excel(path)
print(data)

df = pd.DataFrame(data,columns=['Red','Orange','Yellow','Brown','Blue','Green'])
#n:kích thước mẫu kẹo có màu xanh lá
#N:kích thích mẫu kẹo bất kì 

n=df['Green'].count()
N=df['Red'].count()+df['Orange'].count()+df['Yellow'].count()+df['Brown'].count()+df['Blue'].count()+df['Green'].count()

#n =19
#N = 100
#tỉ lệ là 0.19
print('Ti le la :',n/N)

p_mu = n/N
q_mu = 1-p_mu

# N*p_mu >=5
# N*q_mu >=5

if (N*p_mu)>=5 and (N*q_mu) >=5 :
#là giá trị z mà tại đó xác suất <z là 0.025
#máy tính tính theo dạng xác suất tích lũy nghĩa là tính xác suất < 1 giá trị z nào đó

    z_alpha_chia2 = (-1)*st.norm.ppf(.025,0,1)

    print('z_alpha_chia2 :',z_alpha_chia2)
    e=z_alpha_chia2*np.sqrt(p_mu*q_mu/N)

    print('Loi la : ',e)
    print('Khoang tin cay la : ',p_mu-e,p_mu+e)