import pandas as pd
import numpy as np
import matplotlib as mat
from pandas import  DataFrame, Series


# -- To read Happiness Data of all countries and use pivot table to summaize data

data_csv = pd.read_csv('E://Python//Code//Data//Happiness.csv')

pvt = pd.pivot_table(data_csv, index = (['Region']), columns = 'Year', values= 'Happiness Score')
print(pvt)