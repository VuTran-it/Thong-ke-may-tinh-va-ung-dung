import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st 

# Bài 1 : Gree M&M Candies
path = r'F:\Wed\Python\DataSet\09_MOVIES.xls'
data = pd.read_excel(path)
print(data)

df = pd.DataFrame(data,columns=['Title','MPAA','Budget','Gross','Length','Rating'])

# N là tống các bình chọn
N=df['MPAA'].count()

# n là tống các bình chọn R
df_R = df.query('MPAA=="R"')['MPAA']
n = df_R.count()

print('Ti le binh chon R la :',n/N)

p_mu = n/N
q_mu = 1-p_mu

# N*p_mu >=5
# N*q_mu >=5

if (N*p_mu)>=5 and (N*q_mu) >=5 :
    z_alpha_chia2 = (-1)*st.norm.ppf(.025,0,1)

    print('z_alpha_chia2 :',z_alpha_chia2)
    e=z_alpha_chia2*np.sqrt(p_mu*q_mu/N)

    print('Loi la : ',e)
    print('Khoang tin cay la : ',p_mu-e,p_mu+e)

# nhận xét : tỉ lệ bình chọn R là : 34.28%
# Khoang tin cay la :  0.18560355407792442 0.5001107316363613

#viết kết luận : chúng tôi tin tưởng 95% rằng phần trăm phim được 
# bình chọn là R trong khoảng từ : 18.56% đến 50.01%

#Kết luận : vậy hầu hết các phim bình chọn khác R. vì theo mẫu thì bình chọn R chỉ 
# chiếm 34.28% và tin tưởng 95% rằng phần trăm phim được bình chọn là R trong khoảng từ : 18.56% đến 50.01%