import numpy as np 
so_lan_tung=10000
tung_dong_xu = np.random.randint(2, size=so_lan_tung)
so_lan_0 = (tung_dong_xu == 0).sum()
so_lan_1 = (tung_dong_xu == 1).sum()
P_0 = so_lan_0/so_lan_tung
P_1 = so_lan_1/so_lan_tung
print(P_0)
print(P_1)
