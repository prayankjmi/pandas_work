'''
Created on Apr 18, 2018

@author: Prayank
'''
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from pandas import  DataFrame, Series
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split


train_data = pd.read_csv('E://Python/Code/Data/ML/train.csv')
print(train_data.head(5))

# Data Cleaning
# 1 : Separate Attributes and Label


train_label = train_data['Survived']
train_attr = train_data[:]
del train_attr['Survived']


# 2 : Remove unwanted Columns from train attributes like Passenger name etc

del train_attr['Name']
del train_attr['Ticket']


# 3 : Split gender columm 'Sex' into 2 values 'male and female'
attr_gender = list(train_attr['Sex'])

gender_norm = []
for i in attr_gender:
    if (i =='male'):
        l = [1,0]
    else:
        l = [0,1]
    gender_norm.append(l)

attr_gender['male'] = gender_norm[]


    


