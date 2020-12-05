# python3 setup.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('func.pyx', language_level="3"))
# setup(ext_modules=cythonize('func_2.pyx'))
