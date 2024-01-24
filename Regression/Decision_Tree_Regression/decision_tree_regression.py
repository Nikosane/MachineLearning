# -*- coding: utf-8 -*-
"""Decision-Tree-Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y1CKUgvyr9E69FckyrA1bjC57Gzs_5e4

# **import the libraries**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""# **Load the data**"""

df = pd.read_csv('Position_Salaries.csv')
x = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

"""# **Apply the Decision tree Regression**"""

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x,y)

"""# **testing the Decision tree result**"""

regressor.predict([[6.5]])

"""# **Visualising the Decision Tree result**"""

x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color="red")
plt.plot(x_grid, regressor.predict(x_grid).reshape(-1,1))
plt.title("truth or bluff(Decision tree regression)")
plt.xlabel("level")
plt.ylabel("salaries")
plt.show(

)

