import numpy as np 
so_lan_tung=10000
def tung_xu() :
    if np.random.random() < 0.6:
        return 0
    else : 
        return 1
ket_qua=np.zeros(so_lan_tung)
for i in range (so_lan_tung):
    ket_qua[i]=(tung_xu())

P_3=(ket_qua == 0).sum()/so_lan_tung
P_4=(ket_qua == 1).sum()/so_lan_tung
print(P_3)
print(P_4)