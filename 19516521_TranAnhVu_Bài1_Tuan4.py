import numpy as np 

array_random = np.random.randint(low=0,high=100,size=(12,12),dtype="int32")

print (array_random)
print("kieu du lieu cua mang : ",array_random.dtype)
print("kich thuoc cua mang : ",array_random.shape)
print("So phan tu cua mang   : ",array_random.size)
print("So chieu cua mang   : ",array_random.ndim)

print("======================================")
len = len(array_random[0])
print("Phan tu nam tren duong cheo chinh :",[array_random[i][i] for i in range(len)])
print("Phan tu nam tren duong cheo phu :",[array_random[len-i-1][len-i-1] for i in range(len)])

print("======================================")
array_random = np.random.randint(low=0,high=100,size=(12,12),dtype="int32")
print(array_random)
len = len(array_random[0])
x = int(input("Nhap so gia tri cuar x : "))

nho = 0 
bang = 0 
lon = 0 
for i in range (len) :
    for j in range (len) :
        if(array_random[i][j] == x) :
            bang += 1
        elif(array_random[i][j] < x) :
            nho += 1
        else:
            lon += 1
        
print('so phan tu bang x trong ma tran : ',bang)
print('so phan tu nho hon x trong ma tran : ',nho)
print('so phan tu lon hon x trong ma tran : ',lon)