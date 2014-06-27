import numpy as np
from scipy.optimize import curve_fit

def Fx(x,a,b,c):                 #This is the function that is defined
    return a*np.exp(-b*x) + c

def newFit():
    '''Module that asks for initial "clean" values, creates data with noise
    and fits the data. The returned values is an array of the fit coefficients'$
    a=input("Amplitude a=")
    b=input("Decay 1/tau =")
    c=input("Intercept c=")

    xdata = np.linspace(0,4,50)
    y = Fx(xdata,a,b,c)
    ydata = y+0.2*np.random.normal(size=len(xdata))

    popt,pcov = curve_fit(Fx,xdata,ydata)
    return popt
