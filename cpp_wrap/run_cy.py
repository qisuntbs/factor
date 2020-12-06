#!/usr/bin/python3
from cylink import cyfunc
from numpy import nan

# you will still have to import the c++ class by calling cyfunc()
cy_data = cyfunc()

data = cy_data.get_double("data.csv".encode('utf-8'))
