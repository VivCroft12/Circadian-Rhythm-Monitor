import numpy as np
import pandas as pd
x = pd.read_csv('example_activity_data.csv')

new_x = x.T
new_x1 = new_x[[0,1,2]]
final_x = new_x1.T
p = len(final_x.columns)
xh = final_x.mean()
v = np.array(final_x.T)
n = v.size
numerator = np.sum(np.power((xh - np.mean(v)),2))/p
denominator = np.sum(np.power((v - np.mean(v)),2))/n
print(numerator/denominator)