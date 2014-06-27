import numpy as np
from scipy.optimize import curve_fit


def D431_y(v):
    Cc = np.exp(-1.14883-2.65868*v)
    Dd = np.exp(-0.0038138-12.5645*v)
    Ee = np.exp(5.46491 - 37.6289*v)
    Ff = np.exp(13.0458 - 37.6289*v)
    Gg = np.exp(37.4619 - 192.643*v)
    Hh = np.exp(80.4945 - 400.468*v)

    Zz = v + 0.7 + Cc - Dd + Ee - Ff + Gg - Hh

    return np.log10(np.log10(Zz))

def D431L_y(vl):
    retList=[]
    for v in vl:
        retList.append(D431_y(v))
    return retList

def D431L_x(tl):
    retList=[]
    for t in tl:
        retList.append(D431_x(t))
    return retList

def listable(functionName, listName):
    retList=[]
    for l in listName:
        retList.append(functionName(listName))
    return retList
    
    
def D431_x(t):
    if t < 300:                 # t is probably in C
        T = t + 273.15
    else:                       # t is probably in kelvin
        T = t

    return np.log10(T)


def FVisc(x,A,B):
    return A - B*x


def enterMultipointCalibration():
    ind = 1
    visc=[]
    ts=[]
    while True:
        v = raw_input("Enter viscosity value for point %s: " % ind)
        if v.isdigit() is False:
             break
        t = raw_input("Enter temperature value for point %s: " % ind)
        if t.isdigit() is False:
             break
        ind += 1
        if v:
            visc.append(v)
            ts.append(t)
        else:
            break

    yData = D431_y(visc)
    xData = D431_x(ts)



