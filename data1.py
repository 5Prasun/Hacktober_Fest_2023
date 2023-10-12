#importing the data set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#imporing the dataset
dataset=pd.read_csv('data.csv')
x=dataset.iloc[:, :-1].values
y=dataset.iloc[:,-1].values

#printing the dataset
print(x)
print(y)

#taking care of the missing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

#print the missing data
print(x)