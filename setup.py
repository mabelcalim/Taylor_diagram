# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:03 2013

@author: Mabel Calim Costa
"""

import os
from setuptools import setup
#from distutils.core import setup

for line in open('__init__.py').readlines():
    if line.startswith('__version__'):
        exec(line.strip())

setup(
    name = "taydiag",
    description = ("Taylor diagram in python"),
    version=__version__,
    author='Mabel Calim Costa',
    author_email='mabelcalim@gmail.com',
    #url='https://wavelet-analysis.readthedocs.org/en/latest/index.html',
    url = 'https://github.com/mabelcalim/Taylor_diagram',
    #packages=['' ],
    package_dir={'':'lib'},
    classifiers=[
	'License :: GNU version 3'],
)

