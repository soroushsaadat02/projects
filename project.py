import pandas as pd
import yfinance as yf

#GC=F = Gold , CL=F = Oil , DX-Y.NYB = $
symbols = [ 'GC=F' , 'CL=F' , 'DX-Y.NYB']
dataset = pd.DataFrame()

for symbol in symbols:
    data = yf.download(symbol , start = '2021-01-01' , end = '2023-12-01')
    data.reset_index(inplace = True)
    data['Object'] = symbol
    data.index = data.Date
    data.drop('Date', axis = 1 , inplace = True)
    data.drop('Adj Close', axis = 1 , inplace = True)    
    data = data.replace('', None) 
    dataset = pd.concat([dataset , data])
   
dataset.to_csv('task 9.csv' ,index = True)






