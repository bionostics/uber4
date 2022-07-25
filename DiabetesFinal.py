import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import sklearn.metrics
from numpy import ravel
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("/Users/mvideet/PycharmProjects/CAC/diabetes.csv")
df = df.drop_duplicates()
df.drop('PhysHlth',inplace=True, axis=1)
df.drop('Education',inplace=True, axis=1)
df.drop('Income',inplace=True, axis=1)
df.drop('CholCheck',inplace=True, axis=1)
non_dia= df[df['Diabetes_012'] == 0]
pre_dia = df[df['Diabetes_012'] == 1]
dia = df[df['Diabetes_012'] == 2]
pre_dia_os = pre_dia.sample(len(non_dia), replace=True)
dia_os = dia.sample(len(non_dia), replace=True)
df_new = pd.concat([pre_dia_os,dia_os, non_dia], axis=0)
df_new['Diabetes_012'].value_counts()
y=df_new.iloc[:,:1]
x = df_new.iloc[:, 1:]
print((y.iloc[1]))
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=(0.2))
scaler=MinMaxScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(x_train),columns=x_train.columns)
X_test_scaled = pd.DataFrame(scaler.transform(x_test),columns=x_test.columns)
from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier(n_estimators=100,
                                 min_samples_split=5, random_state=0)
model.fit(X_train_scaled, y_train.values.ravel())
joblib.dump(model, 'diabetes.pkl')
input = pd.DataFrame([[1.0, 0.0, 28.0, 0.0, 0.0, 0.0, 10., 1, 1, 0, 1, 0, 1, 0, 0, 1, 11]], columns = ['HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'DiffWalk', 'Sex', 'Age']
)

predictions = model.predict(X_test_scaled)
print(predictions)
y_pred = model.predict(input)
print(y_pred)
print(metrics.accuracy_score(y_test,predictions))
