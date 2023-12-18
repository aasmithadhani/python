# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.loc[0])

import pandas as pd
df = pd.read_csv('C:/Users/aasmi/Desktop/SEM 5/PYTHON/Pandas&Matplot/dataset.csv')
print(df.head())
print(df.describe())


import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()

z = np.array([35, 25, 25, 15])
plt.pie(z)
plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()