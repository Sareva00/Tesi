
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


def Ng(x):

    z = np.array([1,1.2,1.4,1.6])
    n = np.array([6.86,5.58,4.21,2.61])
    for i in range (len(z)):
        z[i]= (round(z[i],1))
    ng =  interpolate.interp1d(z,n,kind='cubic')
    y = float(ng(x))
    return y

def b(x):
    b = np.array([1.46,1.61,1.75,1.90])
    z = np.array([1,1.2,1.4,1.6])

    for i in range (len(z)):
        z[i]= (round(z[i],1))

    bz =  interpolate.interp1d(z,b,kind='cubic')
    y = float(bz(x))
    return y

def Vol(x):
    V = np.array([7.94,9.15,10.05,16.22])
    V = V*0.21886*4*np.pi;
    z = np.array([1,1.2,1.4,1.6])

    for i in range (len(z)):
        z[i]= (round(z[i],1))

    vol =  interpolate.interp1d(z,V,kind='cubic')
    y = float(vol(x))
    return y

