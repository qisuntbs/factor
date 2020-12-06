# distutils: language = c++

from libcpp.string cimport string
from libcpp.vector cimport vector
from cppfunc cimport cppfunc

cdef class cyfunc:
    cdef cppfunc cyt

    def __cinit__(self):
        self.cyt = cppfunc()

    def get_str_data(self, string file_name):
        return self.cyt.data_as_string(file_name)

    def get_double(self, string file_name):
        return self.cyt.data_as_double(file_name)

    def remove_nan(self, vector[vector[double]] data, int num):
        return self.cyt.remove_nan(data, num)
