# Run this as: python setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

modules = [Extension("helloworld", ["helloworld.pyx"])]

setup(name = "HelloWorld", cmdclass = {'build_ext': build_ext}, ext_modules = cythonize(modules))
