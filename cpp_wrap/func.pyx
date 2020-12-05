# distutils: language = c++

from libcpp.string cimport string
from read_csv cimport table

cdef class py_table:
    cdef table cyt

    def __cinit__(self, string file_name):
        self.cyt = table(file_name)

    # def data_as_str(self, string file_name):
    #     return self.cyt.data_as_string(file_name)
    def get_data(self, string file_name):
        return self.cyt.data_as_string(file_name)

    def get_double(self, string file_name):
        return self.cyt.data_as_double(file_name)

    # Attribute access
    @property
    def file_name(self):
        return self.cyt.file_name

    @file_name.setter
    def file_name(self, file_name):
        self.cyt.file_name = file_name

    @property
    def data(self):
        return self.cyt.data

    @data.setter
    def data(self, file_name):
        self.cyt.data = self.cyt.data_as_string(file_name)
    
