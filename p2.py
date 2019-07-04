import tensorflow as tf
import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import bs4 as bs

print(plt);
print(mpl.__version__)
print(plt.style.available)
stocks=["UVXY","SVXY"]
start = dt.datetime(2018, 9, 1)
end = dt.datetime.now()
df=pd.read_csv('stocks.txt',parse_dates=True,index_col=0,names=['Date','FXI','MGM'],skiprows=[0,1,2], usecols=[0,3,4])
#df=pd.read_csv('stocks.txt',parse_dates=True,index_col=0)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
#df = df.drop("Low", axis=1)
print(df)
df['label']=df['MGM'].shift(-1)
print(df)
#print(df['Adj Close'])
df.plot()
df['Adj Close'].plot()
plt.show()
last_date=df.iloc[-2].name
last_unix=last_date.timestamp()
print(last_date)
print(last_unix)