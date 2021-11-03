import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st 

# Bài 2 : Freshman Weight Gain
path = r'F:\Wed\Python\DataSet\03_FRESH15.xls'
data = pd.read_excel(path)
print(data)

df = pd.DataFrame(data,columns=['WTSEP','WTAPR','BMISP','BMIAP'])
# cân nặng tháng 9 : WTSEP
# cân nặng tháng 4 : WTAPR

N=df['WTSEP'].count()
print('Tong dong : ',N)

df_tang = df.query('WTSEP>WTAPR')['WTSEP']
n = df_tang.count()

#df_tang = df_.query('BMISP > BMIAP')

print('n = ',df_tang.count())

print('Ti le la : ',n/N)
p_mu = n/N
q_mu = 1 - p_mu

if (N*p_mu)>=5 and (N*q_mu) >=5 :
#là giá trị z mà tại đó xác xuất <z là 0.025
#máy tính tính theo dạng xác suất tích lũy nghĩa là tính xác xuất <1 giá trị
    z_alpha_chia2 = (-1)*st.norm.ppf(.025,0,1)

    print('z_alpha_chia2 :',z_alpha_chia2)
    e=z_alpha_chia2*np.sqrt(p_mu*q_mu/N)

    print('Loi la : ',e)
    print('Khoang tin cay la : ',p_mu-e,p_mu+e)

#viết kết luận : chúng tôi tin tưởng 95% rằng phần trăm sinh viên tăng cân trong năm nhất 
#nằm trong khoảng từ : 14.95% đến 35.79%
#kết quả trên máy tính là : 0.14953671015835032 đến 0.35792597640881385