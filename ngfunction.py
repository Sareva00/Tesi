
import camb
from camb import model, initialpower
from camb.sources import GaussianSourceWindow, SplinedSourceWindow
import numpy as np
import sympy as sy
from sympy import symbols
from scipy import interpolate
from scipy import optimize
import matplotlib
from matplotlib import pyplot as plt

z = np.arange(0.7,2.1,0.1)
n = np.array([17.5,19,18,16,15,13.2,12,10,7.5,5.5,3.5,3.2,2,1])

ng =  interpolate.interp1d(z,n,kind='cubic')

def Ng(x):
    ng =  interpolate.interp1d(z,n,kind='cubic')
    y = float(ng(x))
    print(y)
    return y