import numpy as np
import math
from scipy import stats
from func_chamada_call import call3

#definindo das constantes do programa principal
S=40
K=42
T=0.5
r=0.015
sigma=0.2
c0=1.6
#Newton Raphson para calcular a volatilidade impilcito
tol=1e-3
delta=1
cont=0
max_it=100
vol=0.5

while delta>tol:
    cont=cont+1
    if cont>max_it:
        print('máximo de iterações')
        break;
    vol_anterior=vol
    c,d1 = call3(S,K,T,r,vol)
    funcao=c-c0
    vega = S*stats.norm.pdf(d1)*np.sqrt(T)
    vol=vol-funcao/vega
    delta=abs((vol-vol_anterior)/vol_anterior)

print('+++++++++++++++++++++++++++++++++++++++')
print('preço call',round(c,5))
print('volatilidade =',round(vol,3))
print('interações =', cont)