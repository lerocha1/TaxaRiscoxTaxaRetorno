import pandas_datareader as pdr
import  pandas as pd
import datetime
import yfinance as yf


vale3 = pdr.get_data_yahoo('VALE3.SA',start = datetime.datetime(2016,10,1),end=datetime.datetime(2022,10,31))
#print(vale3)

petr4 = pdr.get_data_yahoo('PETR4.SA', start  = datetime.datetime(2016,10,1), end = datetime.datetime(2022,10,31))
#print(petr4)

bbas3 = pdr.get_data_yahoo('BBAS3.SA', start  = datetime.datetime(2016,10,1), end = datetime.datetime(2022,10,31))
#print

print('+++++++++++++++++++++++++++++++++++++++++ Dados coletados+++++++++++++++++++++++++++++++')
"""
#++++++++++++++++++Criando função para pegar mais de ação+++++++++++
def get(acoes, start, end):
    def data(acoes):
        return (yf.download(acoes, start, end).Close)

    datas = map (data, acoes)
    return  (pd.concat(datas, keys=acoes, names=['Acoes', 'Date']))

acoes = ['VALE3.SA','PETR4.SA','BBAS3.SA']
start  = datetime.datetime(2016,10,1)
end = datetime.datetime(2022,10,31)

dados = get(acoes, start, end)


print(dados.head(50))

vale3.drop(['High','Low','Open', 'Volume','Adj Close'], axis=1, inplace=True)
petr4.drop(['High','Low','Open', 'Volume','Adj Close'], axis=1, inplace=True)
bbas3.drop(['High','Low','Open', 'Volume','Adj Close'], axis=1, inplace=True)
"""

closevale = vale3['Close']

closepetr4 = petr4['Close']


clopsebbas3 = bbas3['Close']

print('+++++++++++++++++++++++++++++++++++++++++Dados Filtrados+++++++++++++++++++++++++++++++')

tudo1 = pd.merge(closevale, closepetr4, left_index=True, right_index=True)
print('+++++++++++++++++++++++++++++++++++++++++Dados Merge 1+++++++++++++++++++++++++++++++')

tudo = pd.merge(tudo1, clopsebbas3, left_index=True, right_index=True)
all = tudo.rename(columns={'Close_x':'Vale', 'Close_y':'Petr4','Close':'BBAS3'})


print(all.tail(20))

import matplotlib.pyplot as fig

fig.plot(all)
fig.legend(all)
fig.xlabel('Período')
fig.ylabel('Valor (R$)')
fig.title('Ativos Bovespa - 2016 - 2022', fontsize=16)
fig.grid()



n=len(all)
#prec = all.drop(['Date'], axis=1)
ri = all/all.shift(1)-1
mi=ri.mean().values*252
sigma = ri.cov()*252
print('***********************Matriz de covariancia da carteira*************************')
print(sigma)


fig.show()