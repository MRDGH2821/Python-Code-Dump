import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("E:\\EBOOKS\\GedIT\\Admission.csv")
Lreg = LinearRegression()
# Removing Missing Entry
print(df.head())
print(df.shape)
df = df.dropna()
print(df.shape)
x = np.asarray(df.iloc[:, 1:8])
y = np.asarray(df.iloc[:, -1])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
Lreg.fit(X_train, y_train)
print(Lreg.score(X_train, y_train))
print(Lreg.coef_)
