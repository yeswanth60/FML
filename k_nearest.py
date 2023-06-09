# -*- coding: utf-8 -*-
"""k-nearest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DfUaJ77d2FiO5nJb7k-AmFK9gdJp253L
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris=load_iris()

iris.data[:5]

print(iris.target_names)

X=iris.data
y=iris.target
#split the training and testing data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=41)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

KNeighborsClassifier()

y_pred = knn.predict(X_test)

knn.score(X_train, y_train), knn.score(X_test, y_test)

confusion_matrix(y_test, y_pred)

print(classification_report(y_test, y_pred))