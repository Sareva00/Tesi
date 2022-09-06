%matplotlib inline
%config InlineBackend.figure_format = 'retina'
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

it, ax = plt.subplots()

ax.set_xlabel('z')
ax.set_ylabel('n*10^4 [h^3/Mpc^3]')

ax.plot(z, n, color='g', ls ='-')  #aggiungi gli errori

ng =  interpolate.interp1d(z,n,kind='cubic')
plt.plot(z, ng(z), '--')

def Ng (z):
    return ng(z)