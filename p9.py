#import Quandl
import pandas as pd
import pickle

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
df1=fiddy_states[0].drop(0,axis=1)
df2=fiddy_states[1]
#print(fiddy_states[1][1:][1:])
print(df1[0:])
print(df2[0:])