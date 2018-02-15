import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np

x = [5, 10, 15, 20, 24, 30, 35, 39, 45, 48, 53]
y = [40, 62, 85, 93, 111, 126, 136, 154, 166, 180, 190]


model = linear_model.LinearRegression()
model.fit(np.array(x).reshape((11, 1)), y)
print(model.coef_, model.intercept_)
