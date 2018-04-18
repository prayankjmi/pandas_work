import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from pandas import  DataFrame, Series
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

train_x = [i for i  in range(1000)]
train_y = [math.sqrt(x + np.random.rand()) for x in train_x]

X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.33, random_state=42)
lm = LinearRegression()
X = np.array(X_train)
X = X.reshape(-1,1)
t = lm.fit(X, y_train)


lm.normalize()




