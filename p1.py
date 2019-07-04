import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

print(plt);
print(mpl.__version__)
print(plt.style.available)
stocks=["UVXY","SVXY","FAS","QLD","QQQ","CHAU","FXI","UCO","MGM"]
start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()
df = web.DataReader(stocks, 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df.to_csv('stocks_1.txt')
#df=pd.read_csv('stocks.txt',parse_dates=True,index_col=0)
#df = df.drop("Low", axis=1)
print(df['High'].head())
print(df['Adj Close'].tail())
#df['High'].plot()
df['Adj Close'].plot()
plt.show()
