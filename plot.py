import pandas as pd
import numpy as np
import matplotlib as mat
from pandas import  DataFrame, Series




data_csv = pd.read_csv('E://Python//Code//Data//Happiness.csv')

print(data_csv.plot())