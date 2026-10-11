

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as linalg
import seaborn as sns



def build_library(x):

    """
    build a function library based on statevector timeseries
    """

    
    n = len(x)
    variable = ['1', 'x', 'xy', 'xz', 'y', 'yz', 'z']
    names = ["1"]

    Theta= [np.ones_like(x[0])]

    for i in range(n):
        Theta.append(x[i])
        names.append(variable[i])
        for j in range(i, n):
            values = np.array(x[j]*x[i])
            term = "".join([variable[i],variable[j]])
            if j!=i:
                Theta.append(values)
                names.append(term)

    Theta = np.column_stack(Theta)


    return Theta, names

def lsq_regression(Theta, x):
    reg = []
    for _ in range(3):
        regressiondata,_,_,_ = linalg.lstsq(Theta, x[_],rcond=None)
        reg.append(regressiondata)

    x = np.column_stack(reg)
    
    return x

def coeff_thresholding(lstsq_sols,threshhold):
    xdatanew = lstsq_sols.copy()
    n = len(lstsq_sols)
    for _ in range(n):
    # using a mask : set those entries of xdata[_] less than the threshhold to zero
        xdatanew[_][np.abs(lstsq_sols[_])<threshhold] = 0
    return xdatanew

# reference = xdata.copy()

def thresholds(Theta, xdot, xdata, thresholds):

    model_selections = []
    for l in thresholds:
        for m in range(10):
            xdata = lsq_regression(Theta,xdot)
            xdata[np.abs(xdata)<l] = 0
        model_selections.append(xdata)
    return model_selections



def read_data():
    df = pd.read_csv(r"..\lorenz_data.csv")

    t = df["t"].to_numpy()

    x = df["x"].to_numpy()
    y = df["y"].to_numpy()
    z = df["z"].to_numpy()
    x = [x,y,z]

    xdot = df["x_dot"].to_numpy()
    ydot = df["y_dot"].to_numpy()
    zdot = df["z_dot"].to_numpy()
    xdot = [xdot,ydot,zdot]
    return t, x, xdot

def show_lorenztime(t,x,xdot):

    """
    Plots time series data for each component of the statevector
    """


    fig,ax = plt.subplots(3,1)

    for _ in range(3):
        ax[_].plot(t,x[_])
        ax[_].plot(t,xdot[_],"yo",markersize = 0.1)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(x[0], x[1], x[2])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
