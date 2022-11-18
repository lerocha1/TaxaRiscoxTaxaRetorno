import numpy as np
import pandas as pd

#******************************nomes dos ativos+++++++++++++++++++

ativo = ['A', 'B', "C"]
n=len(ativo)

#construção dos ativos +++++++++++
A= np.array([4,5,6,5,5,6,7,8,4,3,5])
B= np.array([1,5,10,4,11,7,8,3,1,5,7])
C= np.array([3,4,3,4,5,6,5,3,5,3,4])

#++++Dataframe dos ativos com Pndas+++++++

df = pd.DataFrame([A,B,C], index=ativo)
prec = df.T #transposta para colocar dados em colunas

print(prec)


#++++++++++++Retorno dos preços++++++++++++++
ri = prec/prec.shift(1)-1
mi=ri.mean() #retorno médio dos ativos por colunas
sigma=ri.cov()  #covariancia da carteira

print(sigma)

#w=np.array([0.6,0.3,0.1]) PAra um array especifico

#w=np.random.random(n) Para um array random
#w=w/np.sum(w)

#Trocando para um loop randomico com range de 200 passos
vet_R = []
vet_vol = []

for i in range (200):
    #++++Pesos da alocação dos investimentos+++++++
    w = np.random.random(n)
    w = w/np.sum(w)
    #++++++++++++++retorno e risco da carteira+++++++++++++
    retorno = np.sum(w * mi)
    risco = np.sqrt(np.dot(w.T, np.dot(sigma, w)))
    #++++++++++++++++++++++++++++++++++++++++++++++++++
    vet_R.append(retorno)
    vet_vol.append(risco)


#retorno = np.sum(w*mi)
#risco=np.sqrt(np.dot(w.T, np.dot(sigma,w)))
print('A taxa de Retorno é de ', str(round(retorno*100,2)),'%')
print('O risco é de ', str(round(risco*100,2,)),'%')

import matplotlib.pyplot as fig

fig.plot(vet_vol, vet_R, 'ok')
fig.grid()
fig.xlabel('Volatilidade Esperada')
fig.ylabel('Retorno Esperado')
fig.show()

