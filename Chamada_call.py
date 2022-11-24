import numpy as np
import math
from scipy import stats
from func_chamada_call import call, call2
"""
c=call(40,42,0.5,0.015,0.2)
print('')
print('++++++++++++++++++++preço da call++++++++++++++++++++++')
print('call = ',round(c,3))
"""

c1=call2(40,42,0.5,0.015,0.2)
print('')
print('++++++++++++++++++++preço da call++++++++++++++++++++++')
print('call = U$',round(c1,2))
