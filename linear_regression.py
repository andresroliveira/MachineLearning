import numpy as np
import pandas as pd

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

cut = {
    '"Ideal"': 5,
    '"Premium"': 4,
    '"Very Good"': 3,
    '"Good"': 2,
    '"Fair"': 1
}
color = {'"D"': 7, '"E"': 6, '"F"': 5, '"G"': 4, '"H"': 3, '"I"': 2, '"J"': 1}
clarity = {
    '"IF"': 8,
    '"VVS1"': 7,
    '"VVS2"': 6,
    '"VS1"': 5,
    '"VS2"': 4,
    '"SI1"': 3,
    '"SI2"': 2,
    '"I1"': 1
}

# convert.csv collums with string into new_diamonds.csv collums floats

# with open('diamonds.csv', 'r') as r, open('new_diamonds.csv', 'w') as w:
#     rl = r.readline()
#     wl = ','.join(rl.split(',')[1:])
#     w.write(wl)
#     rl = r.readline()
#     cont = 0
#     while rl.find(',') >= 0:
#         wl = rl.split(',')[1:]
#         wl[1] = str(cut[wl[1]])
#         wl[2] = str(color[wl[2]])
#         wl[3] = str(clarity[wl[3]])
#         wl = ','.join(wl)
#         w.write(wl)
#         rl = r.readline()

data = pd.read_csv('new_diamonds.csv', dtype=float)
print(data)

y_data = data.pop('price')
x_data = data

print(x_data.to_numpy())
print(y_data.to_numpy())
