from matplotlib import colors
import numpy as np
from numpy.core.fromnumeric import mean
from numpy.random.mtrand import random_sample, sample 
import scipy.stats as stats
import matplotlib.pyplot as plt

# mô phỏng tung đồng xu 4 lần
np.random.seed(10)

#In 2 số ngẫu nhiên trong khoảng (0,1)
print(np.random.random())
print(np.random.random())

#Phát sinh 4 số ngẫu nhiên trong khoảng (0,1)
arr = np.random.random(size=4)
print(arr)

#tạo mẫu mô phỏng 4 lần tung đồng xu với (True : sắp, False : Ngửa)
coin_sample = arr < 0.5
print(coin_sample)

""" VD1 : sử dụng ước lượng điểm đề ước lượng tham số của quần thể """
#Khởi tạo một phần thể cho trước thể hiện chiều cao(cm) của 5 thanh
SMALL_POP = np. array([186,182,157,158,152])
print(SMALL_POP)
maen_of_SMALL_POP = np.mean(SMALL_POP)
print('Chiều cao trung bình của quần thể : {}'.format(maen_of_SMALL_POP))

#lấy ngẫu nhiên một mẫu có kích thước là 4, và tính chiều cao trung bình và so sánh với giá trị của quần thể
np.random.seed(24)
sample1 = np.random.choice(SMALL_POP, size=4,replace=True)
sample1_mean = np.mean(sample1)
print('Mẫu ngẫu nhiên 1 : ', sample1)
print('Chiều cao trung binh của mẫu 1 :{}'.format(sample1_mean))
print('Sai số ước lượng : {}'.format(abs(sample1_mean-maen_of_SMALL_POP)))


#Nhận xét : sai số ước lượng là : 3.75cm. Ta có thể chấp nhận được với bài toán đo chiều cao

""" VD2: Để cho việc do sai số khách quan, ta thử lặp lại việc lấy mẫu trên 10 lần, và tính sai số ước lượng """

mean_array = np.empty(10)
for i in range(10):
    random_sample = np.random.choice(SMALL_POP,size=4,replace=True)
    random_sample_mean = np.mean(random_sample)
    mean_array[i] = random_sample_mean

print('Chiều cao trugn bình của 10 mẫu thử được : ',mean_array)
print('Sai số ước lượng : {}'.format(abs(np.mean(mean_array) - maen_of_SMALL_POP)))

#Nhận xét : ta nhận thấy, khi thực hiện việc lấy mẫu nhiều lần, sai số trung bình có nhỏ hơn so với ví dụ trên


""" 
VD3 : Minh hoạ ảnh hưởng của cỡ mẫu đến độ chính xác của ước lượng
o Để rõ ràng ta sẽ tạo một quần thể mới gồm 100 cá thể: MEDUIUM_POP
o Lần lượt lấy mẫu với kích cỡ khác nhau sample_size = 1, 2, 3, ... và tính
trung bình mẫu: mean_array
o Trực quan bẳng đồ thị 
"""
MEDIUM_POP = np.random.randint(130,200,size=100)
maen_of_MEDIUM_POP = np.mean(MEDIUM_POP)
mean_array = np.empty(100)
mean_array[0]=0

for sample_size in range(1,100):
    temp = np.random.choice(MEDIUM_POP,size=sample_size)
    mean_array[sample_size] = np.mean(temp)

x = np.arange(100)
_ = plt.plot(x,mean_array,marker='.',color='black')

_=plt.xlabel('Kích cỡ mẫu (0-100')
_=plt.ylabel('Chiều cao trung bình của mẫu (cm)')
_=plt.title('Ảnh hưởng của kích cỡ mẫu đến độ chính xác của ước lượng điểm')

xx = np.array([0,100])
yy=np.empty(2)
yy[0] = yy[1] = maen_of_MEDIUM_POP

_=plt.plot(xx,yy,color='green')
print(mean_array)
plt.show()
#Nhận xét : qua ví dụ trên ta có thể thấy kích thước mẫu có liên quan đến độ chính xác của ướng lượng điểm
#Kết luận : để tăng dộ chính xác của ước lượng ta cso thể tăng kích thước của quần thể
