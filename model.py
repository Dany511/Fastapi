# -*- coding: utf-8 -*-
"""Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WQRGoaTJ7hdj9MRnzAOHNlRXhA5C3VyE
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("Churn.csv")
df.head()

le=LabelEncoder()
df['gender']=le.fit_transform(df['gender'])
df['PhoneService']=le.fit_transform(df['PhoneService'])
df['Churn']=le.fit_transform(df['Churn'])

df['TotalCharges']=df['TotalCharges'].replace({' ':'0'})
df['TotalCharges']=df['TotalCharges'].astype(float)

X=df[['tenure','MonthlyCharges','TotalCharges','gender','PhoneService']]
y=df['Churn']

X

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
lr=LogisticRegression(fit_intercept=True,max_iter=10000)
lr.fit(x_train,y_train)

def predict(x):
   pred=lr.predict(x)
   return pred

print(predict(x_test))