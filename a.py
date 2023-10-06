import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("headbrain6.csv")
x=data.iloc[:,2:3].values
y=data.iloc[:,3:4].values
model = LinearRegression()
model.fit(x,y)
y_pred =model.predict([[number]])
print(y_pred)
