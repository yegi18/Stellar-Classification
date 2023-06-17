# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 01:56:37 2023

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

data=pd.read_csv("D:\\new_downloads\\stellar_data.csv")

x=data.loc[:, data.columns != 'Star color']
x=x.loc[:, x.columns != 'Spectral Class']
print(x)
x.head()
import sklearn
from sklearn.model_selection import train_test_split

x=x.loc[:,x.columns!='Star type']
y=data.loc[:,"Star type"]

train_features, test_features, train_labels, test_labels = sklearn.model_selection.train_test_split(x, y, test_size = 0.25, random_state = 42)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators = 100, random_state = 42)
rf.fit(train_features, train_labels);
predictions = rf.predict(test_features)



test_labels=test_labels.to_numpy()
count=0
for i in range(0,60):
  if predictions[i]!=test_labels[i]:
    count=count+1
err=(count/60)*100
print(predictions)
print(err)
x1=data.loc[:,"Temperature (K)"]
x1=x1.to_numpy()
x1=x1.reshape(-1,1)
y2=data
y2.loc[y2["Spectral Class"] == "O", "Spectral Class"] = 0
y2.loc[y2["Spectral Class"] == "B", "Spectral Class"] = 1
y2.loc[y2["Spectral Class"] == "A", "Spectral Class"] = 2
y2.loc[y2["Spectral Class"] == "F", "Spectral Class"] = 3
y2.loc[y2["Spectral Class"] == "G", "Spectral Class"] = 4
y2.loc[y2["Spectral Class"] == "K", "Spectral Class"] = 5
y2.loc[y2["Spectral Class"] == "M", "Spectral Class"] = 6
y1=y2.loc[:,"Spectral Class"]
train_features1, test_features1, train_labels1, test_labels1 = sklearn.model_selection.train_test_split(x1, y1, test_size = 0.25, random_state = 42)
from sklearn.ensemble import RandomForestClassifier
rf1 = RandomForestClassifier(n_estimators = 100, random_state = 42)
train_labels1=train_labels1.astype('int') 
rf1.fit(train_features1, train_labels1);
predictions1 = rf1.predict(test_features1)

count1=0;
test_labels1=test_labels1.to_numpy()
count1=0
for j in range(0,60):
  if predictions1[i]!=test_labels1[i]:
    count1=count1+1
err1=(count1/60)*100
print(predictions1)
print(err1)
