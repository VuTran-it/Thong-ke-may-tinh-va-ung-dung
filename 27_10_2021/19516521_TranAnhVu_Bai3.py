import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st 

#  bài 3. Lượng mưa ở Boston
path = r'F:\Wed\Python\DataSet\14_BOSTRAIN.xls'
data = pd.read_excel(path)
print(data)

df = pd.DataFrame(data,columns=['MON','TUES','WED','THURS','FRI','SAT','SUN'])

#mưa trong các ngày Thứ Tư
n_web=df['WED'].count()
print('Số ngày mưa là ngày Thứ Tư = ',n_web)
#mưa trong các ngày chủ nhật
n_sun=df['SUN'].count()
print('Số ngày mưa là ngày Chu nhat= ',n_sun)

N=df['MON'].count() + df['TUES'].count() + df['WED'].count() + df['THURS'].count() + df['FRI'].count() + df['SAT'].count() + df['SUN'].count()
print('Tổng các ngày mưa ',N)

print('Ti le la ngay thứ 4 : ',n_web/N)
print('Ti le la ngay thứ chủ nhật : ',n_sun/N)

p_mu_web = n_web/N
q_mu_web  = 1 - p_mu_web

if (N*p_mu_web)>=5 and (N*q_mu_web) >=5 :
    z_alpha_chia2 = (-1)*st.norm.ppf(.025,0,1)

    print('z_alpha_chia2 :',z_alpha_chia2)
    e_web=z_alpha_chia2*np.sqrt(p_mu_web*q_mu_web/N)

    print('Loi la : ',e_web)
    print('Khoang tin cay (ngày thứ tư) la : ',p_mu_web-e_web,p_mu_web+e_web)

#Ti le la ngay thứ 4 :  14.52% (0.14520547945205478)
#Loi la :  0.03614298571970725
#viết kết luận : chúng tôi tin tưởng 95% rằng phần trăm trời mưa vào ngày thứ tư là : 10.91% đến 18.13%
#kết quả trên máy tính là : 0.10906249373234753 đến 0.18134846517176204
print('=====================================================================')
p_mu_sun = n_sun/N
q_mu_sun  = 1 - p_mu_sun
if (N*p_mu_sun)>=5 and (N*q_mu_sun) >=5 :
    z_alpha_chia2 = (-1)*st.norm.ppf(.025,0,1)

    print('z_alpha_chia2 :',z_alpha_chia2)
    e_sun=z_alpha_chia2*np.sqrt(p_mu_sun*q_mu_sun/N)

    print('Loi la : ',e_sun)
    print('Khoang tin cay (ngày thứ tư) la : ',p_mu_sun-e_sun,p_mu_sun+e_sun)

#Ti le la ngay thứ chủ nhật :  14.24% (0.14246575342465753)
#Loi la : 0.03585771696800241
#viết kết luận : chúng tôi tin tưởng 95% rằng phần trăm trời mưa vào ngày chủ nhật là : 10.66% đến 17.83%
#kết quả trên máy tính là : 0.10660803645665512 đến 0.17832347039265994

#So sánh kết quả : tỉ lệ mưa ngày thứ tư và ngày chủ nhật xấp xỉ nhau (T4 : 14.52% > CN:14.24%)

n_mon=df['MON'].count()
print('Tỉ lệ mưa các ngày thứ hai: ',n_mon/N)

n_tues=df['TUES'].count()
print('Tỉ lệ mưa các ngày thứ ba: ',n_tues/N)

n_thurs=df['THURS'].count()
print('Tỉ lệ mưa các ngày thứ năm: ',n_thurs/N)

n_fri=df['FRI'].count()
print('Tỉ lệ mưa các ngày thứ sáu: ',n_fri/N)

n_sat=df['SAT'].count()
print('Tỉ lệ mưa các ngày thứ bảy: ',n_sat/N)

#Lượng các ngày thứ 4 và chủ nhật không phải nhiều hơn các ngày khác mà sấp xỉ bằng nhau 