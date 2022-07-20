import numpy as np
import pandas as pd

data = pd.read_csv('diamonds.csv', index_col=0)

y = data.pop('price')
x = data

print(x)
print(y)

# price : price in US dollars
# carat : Carat weight of the diamond
# cut : Describe cut quality of the diamond. ["Ideal", "Premium", "Very Good", "Good", "Fair"]
# color : Color of the diamond. ["D", "E", "F", "G", "H", "I", "J"]
# clarity : How obvious inclusions are within the diamond. ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]
# depth : total depth percentage = z / mean(x, y) = 2 * z / (x + y)
# table : width of top of diamond relative to widest point
# x : length in mm
# y : width in mm
# z : depth in mm

for d in data:
    arr = list(data[d])
    if isinstance(arr[0], float):
        print(np.sum(arr))
