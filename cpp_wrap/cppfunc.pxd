# distutils: sources = cppfunc.cpp

from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "cppfunc.cpp":
    pass

cdef extern from "cppfunc.h":
    cdef cppclass cppfunc:
        string file_name
        cppfunc() except +

        vector[vector[string]] data_as_string(string)
        vector[vector[double]] data_as_double(string)
        vector[int] remove_nan(vector[vector[double]], int)
