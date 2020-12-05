#!/usr/bin/python3
from func import py_table

cy_data = py_table('data.csv'.encode('utf-8'))

print(dir(cy_data))
# print(cy_data.get_data("data.csv".encode('utf-8')))
print(cy_data.get_double("data.csv".encode('utf-8')))
