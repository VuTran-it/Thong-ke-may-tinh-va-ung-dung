""" câu 1 """
# A : bị bệnh 
# B : dương tính
PrA = 8/500000
PrAc = (500000-8)/500000
PrB_A =  0.55
PrB_Ac = 0.45
# Cần tính PrA_B
PrA_B = (PrB_A * PrA) / (PrB_A*PrA + PrB_Ac*PrAc)

print ("Xác xuất người đó nhiễm Covid là : ",PrA_B)