# -*- coding: utf-8 -*-
"""
Created on Thu Nov 6 2014

@author: Mabel Calim Costa
"""

from __future__ import absolute_import

from .lib.taylor_diag     import load_nc
from .lib.taylor_diag     import Taylor_diag



# Define the objects imported by imports of the form: from pyclimatetools import *
__all__ = ['load_nc', 'Taylor_diag']

# Package version number.
__version__ = '0.0.1.0'
