import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import requests
from scipy.stats import norm
from io import StringIO
import seaborn as sns
import warnings
from func_market_risk import *

warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (10,6)

mean = 0
std_dev = 1
x = np.arange(-5,5,0.01)
y = norm.pdf(x, mean, std_dev)
pdf = plt.plot(x,y)
min_ylim,max_ylim = plt.ylim()
plt.text(np.percentile(x, 5), max_ylim * 0.9, '95%:${:.4f}'
         .format(np.percentile(x, 5)))
plt.axvline(np.percentile(x, 5), color='r', linestyle='dashed', linewidth=4)
plt.title('Exemplo do valor de Risco')
plt.show()

symbols = ['IBM', 'MSFT', 'INTC']
data3 =[]

for symbol in symbols:
    data3.append(getDailyData(symbols)[::-1]['close']['2020-01-01':'2020-12-31'])
    stocks = pd.DataFrame(data3).T
    stocks.columns =symbols


