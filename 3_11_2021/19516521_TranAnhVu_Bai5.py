import pandas as pd
import numpy as np
import scipy.stats as st 

# Bài 5 : tong tien phim
path = r'F:\Wed\Python\DataSet\09_MOVIES.xls'
data = pd.read_excel(path)
print(data)

sigma = 100
df = pd.DataFrame(data,columns=['Title','MPAA','Budget','Gross','Length','Rating'])

# N là tổng số bộ phim
N=df['Gross'].count()
print('Tong so bo phim :',N)

x_gach = df['Gross'].mean()
print('Trung binh la :',x_gach)

z_alpha_chia2 = (-1)*st.norm.ppf(.025,0,1)

print('z_alpha_chia2 :',z_alpha_chia2)
e=z_alpha_chia2*sigma/np.sqrt(N)

print('Loi la : ',e)
print('Khoang uoc luong la : ',x_gach-e,x_gach+e)