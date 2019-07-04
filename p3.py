import numpy
from statistics import mean
import pandas as pd
import quandl
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

df=quandl.get("WIKI/GOOGL")
print(df.head())