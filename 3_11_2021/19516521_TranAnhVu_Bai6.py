import pandas as pd
import numpy as np
import scipy.stats as st 

# Bài 6 : Điểm đánh giá tín dụng FICO
col_name = ['DIEM']
path = r'F:\Wed\Python\DataSet\24_FICO.xls'
data = pd.read_excel(path,names=col_name,header=None)
df = pd.DataFrame(data)
print(df)


# N là tổng số gia tri
N=df['DIEM'].count()
print('Tong :',N)

x_gach = df['DIEM'].mean()
print('Trung binh la :',x_gach)

sigma = 92.2

z_alpha_chia2 = (-1)*st.norm.ppf(0.01/2,0,1)

print('z_alpha_chia2 :',z_alpha_chia2)
e=z_alpha_chia2*sigma/np.sqrt(N)

print('Loi la : ',e)
print('Khoang uoc luong la : ',x_gach-e,x_gach+e)

