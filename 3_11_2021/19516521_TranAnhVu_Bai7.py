import pandas as pd
import numpy as np
import scipy.stats as st 

# Bài 7: Nicotine trong thuốc lá:
# a không lọc, không tẩm bạc hà, và không ánh sáng
path = r'F:\Wed\Python\DataSet\04_CIGARET.xls'
data = pd.read_excel(path)
#print(data)

df = pd.DataFrame(data,columns=['KgTar','KgNic','KgCO','MnTar','MnNic','MnCO','FLTar','FLNic','FLCO'])
print(df)

# N là tổng KgNic
N=df['KgNic'].count()
print('Tong :',N)

x_gach = df['KgNic'].mean()
print('Trung binh la :',x_gach)

s=df['KgNic'].std()
print('Do lech chuan :',s)

t_alpha_chia2 = (-1)*st.t.ppf(.025,N-1,0,1)

print('t_alpha_chia2 :',t_alpha_chia2)
e=t_alpha_chia2*s/np.sqrt(N)

print('Loi la : ',e)
print('Khoang uoc luong la  : ',x_gach-e,x_gach+e)

# b: được lọc, không tẩm bạc hà và không ánh sáng

# N là tổng FLNic
print('===================================================================')
print('CAU B :')
N_FLNic=df['FLNic'].count()
print('Tong :',N_FLNic)

x_gach_FLNic = df['FLNic'].mean()
print('Trung binh la :',x_gach_FLNic)

s_FLNic=df['FLNic'].std()
print('Do lech chuan :',s_FLNic)

t_alpha_chia2_FLNic = (-1)*st.t.ppf(.025,N_FLNic-1,0,1)

print('t_alpha_chia2 :',t_alpha_chia2_FLNic)
e_FLNic=t_alpha_chia2_FLNic*s_FLNic/np.sqrt(N)

print('Loi la : ',e_FLNic)
print('Khoang uoc luong la  : ',x_gach_FLNic-e_FLNic,x_gach_FLNic+e_FLNic)

#c. So sánh kết quả. Bộ lọc trên thuốc lá có vẻ hiệu quả không?

#kết quả từ máy tính :
#Khoang uoc luong la KgNic la :  1.159871648839225 1.3521283511607751
#Khoang uoc luong la FLNic la :  0.813717218547171 1.018282781452829

#Nhận xét ta thấy khoảng ước lương của thước lá có lọc nhỏ hơn khoảng ước lượng không lọc 

# Kết luận : Bộ lọc trên thuốc lá có hiệu quả
