import pandas as pd
import requests
from io import StringIO

def getDailyData(symbol):
    parameters={'function':'TIME_SERIES_DAILY_ADJUSTED',
                'symbol':symbol,
                'outputsize':'full',
                'datatype':'csv',
                'apikey':'88QV0UDS66VHVOZ6'}
    response =requests.get('https://www.alphavantage.co/query', params=parameters)
    csvText = StringIO(response)
    data = pd.read_csv(csvText, index_col='timestamp')
    return data