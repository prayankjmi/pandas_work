import pandas as pd
import numpy as np
import matplotlib as mat
from pandas import  DataFrame, Series
 
from datetime import  datetime


# -- To read Happiness Data of all countries and use pivot table to summaize data

data_csv = pd.read_csv('E://Python//Code//Data//Happiness.csv')

pvt = pd.pivot_table(data_csv, index = (['Region']), columns = 'Year', values= 'Happiness Score')
#print(type(pvt))

pvt.to_csv('E://Python//Code//Data//pivot_happy.csv')


dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
 datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1,
12)]

ts = Series(np.arange(6), index = dates)
print(type(ts))