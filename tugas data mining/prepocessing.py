#import library yang digunakan
import numpy as np
import matplotlib.pylot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, :-1].values
print(x)
print(y)

#splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#menghilangkan missing value (nan)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer (missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(x)
print(y)

#encoding data 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(X)

#Encoding data kategori(Class / Label)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_tansform(y)

#Membagi dataset ke dalam training set dan test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[: 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)
