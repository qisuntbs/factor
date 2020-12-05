#!/usr/bin/python3
from cylink import cyfunc

# you will still have to import the c++ class by calling cyfunc()
cy_data = cyfunc()
print(dir(cy_data))
t = cy_data.get_double("data.csv".encode('utf-8'))

for r in t:
    for c in r:
        print(type(c), '-', c)
