from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Chunker',
    ext_modules=cythonize("chunker.pyx"),
    zip_safe=False,
)