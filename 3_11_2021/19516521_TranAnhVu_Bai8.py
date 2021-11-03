import pandas as pd
import numpy as np
import scipy.stats as st 

# Bài 8: Nhịp tim
# a : nhịp tim trung bình cho nam
print('=========================================================')
print('Nhip tim cua nam')

path = r'F:\Wed\Python\DataSet\01_MHEALTH.xls'
data = pd.read_excel(path)
#print(data)

df = pd.DataFrame(data)
print(df)

# N là tổng so nhịp tim nam
N=df['PULSE'].count()
print('Tong :',N)

x_gach = df['PULSE'].mean()
print('Trung binh la :',x_gach)

s=df['PULSE'].std()
print('Do lech chuan :',s)

t_alpha_chia2 = (-1)*st.t.ppf(.025,N-1,0,1)

print('t_alpha_chia2 :',t_alpha_chia2)
e=t_alpha_chia2*s/np.sqrt(N)

print('Loi la : ',e)
print('Khoang uoc luong nhip tim cua nam la : ',x_gach-e,x_gach+e)


# b : nhịp tim trung bình cho nữ.
print('=========================================================')
print('Nhip tim cua nu')
path = r'F:\Wed\Python\DataSet\01_FHEALTH.xls'
data = pd.read_excel(path)
#print(data)

df = pd.DataFrame(data)
print(df)

# N là tổng so nhịp tim nu
N=df['PULSE'].count()
print('Tong :',N)

x_gach = df['PULSE'].mean()
print('Trung binh la :',x_gach)

s=df['PULSE'].std()
print('Do lech chuan :',s)

t_alpha_chia2 = (-1)*st.t.ppf(.025,N-1,0,1)

print('t_alpha_chia2 :',t_alpha_chia2)
e=t_alpha_chia2*s/np.sqrt(N)

print('Loi la : ',e)
print('Khoang uoc luong nhip tim cua nu la : ',x_gach-e,x_gach+e)

#c. So sánh các kết quả trước đó. Chúng ta có thể kết luận rằng trung bình quần thể cho nam và nữ có khác nhau không? 
# Tại sao có hay tại sao không?

#kết quả từ máy tính : 
#Khoang uoc luong nhip tim cua nam la :  65.78692296923965 73.01307703076036
#Khoang uoc luong nhip tim cua nu la :  72.30274891875666 80.29725108124333

#nhận xét : khoảng ước lượng nhịp tim của nam và nước khác nhau 

#kết luận : trung bình quần thể nam và nữ khác nhau
