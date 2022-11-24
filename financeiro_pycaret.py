import numpy as np

import pandas as pd


data = pd.read_csv(r'C:\Users\leandro.rocha.A1\PycharmProjects\Air_Passengers.csv')
data['Month'] = pd.to_datetime((data['Month']))

data = data.rename({'Month':'Date','#Passengers':'Passangers'})
#print(data.head())

data['M12'] = data['#Passengers'].rolling(12).mean()

print(data.head())

import plotly.express as px

fig = px.line(data, x="Month", y=["#Passengers", "M12"], template='plotly_dark')
fig.show()

data['Month1'] = [i.month for i in data['Month']]

data['Year'] = [i.year for i in data['Month']]

data['Series']=np.arange(1, len(data)+1)


data.drop(['Month', 'M12'], axis=1, inplace=True)

data = data[['Series', 'Year', 'Month1', '#Passengers']]
print(data.head())

#Pedaço de dados para test_train
train = data[data['Year'] < 1960]
test = data[data['Year'] >= 1960]

print(train.shape)
print(test.shape)

from pycaret.regression import *

s=setup(train, test_data=test, target='#Passengers', fold_strategy='timeseries',
        numeric_features=['Year','Series'], fold=3,transform_target=True,session_id=123)

print('Teste finalizado+++++++')

best = compare_models(sort='MAE')

