# -*- coding: utf-8 -*-
"""Rock vs Mine Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BGlBDtshvutaWdRQ1yi3YatsnujEb4ge
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""## **#Data Collection and Data Processing**"""

# Loading dataset
sonar_data = pd.read_csv('/content/sonar.csv', header = None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#Seperating data and labels
X = sonar_data.drop(columns=60, axis=1)
Y= sonar_data[60]

print(X)
print(Y)

"""Training and Testing Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify= Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training = Logistic Regression"""

model = LogisticRegression()

#Model training with Logistic Regression
model.fit(X_train, Y_train)

"""Model Evaluation"""

#Accuracy on data training
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data: ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on testing data: ', test_data_accuracy)

"""Making a Predictive System"""

#Example of datasets
#1. 0.0156,0.0210,0.0282,0.0596,0.0462,0.0779,0.1365,0.0780,0.1038,0.1567,0.2476,0.2783,0.2896,0.2956,0.3189,0.1892,0.1730,0.2226,0.2427,0.3149,0.4102,0.3808,0.4896,0.6292,0.7519,0.7985,0.8830,0.9915,0.9223,0.6981,0.6167,0.5069,0.3921,0.3524,0.2183,0.1245,0.1592,0.1626,0.2356,0.2483,0.2437,0.2715,0.1184,0.1157,0.1449,0.1883,0.1954,0.1492,0.0511,0.0155,0.0189,0.0150,0.0060,0.0082,0.0091,0.0038,0.0056,0.0056,0.0048,0.0024 == M
#2. 0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032 == R


input_data = (0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)

#changing input into array

input_data_array = np.asarray(input_data)

#reshape the np array
input_data_reshaped = input_data_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 'R'):
  print('The object is a rock')
else:
  print('The object is a mine')

