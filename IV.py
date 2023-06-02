import pandas as pd
import numpy as np
x = pd.read_csv('example_activity_data.csv')
y = x.transpose()
temp = np.array(y[0])
index = [0, 1, 2]
new_y = np.delete(temp, index)
mean = np.mean(new_y)
numerator = np.sum(np.power(np.diff(new_y),2))/(new_y.size - 1)
denominator = np.sum(np.power((new_y - mean), 2))/new_y.size
print(numerator/denominator)