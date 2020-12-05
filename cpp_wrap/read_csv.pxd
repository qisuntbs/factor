# distutils: sources = read_csv.cpp

from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "read_csv.cpp":
    pass

cdef extern from "read_csv.h":
    cdef cppclass table:
        string file_name
        table() except +
        table(string) except +

        vector[vector[string]] data
        vector[vector[string]] data_as_string(string)
        vector[vector[double]] data_as_double(string)
