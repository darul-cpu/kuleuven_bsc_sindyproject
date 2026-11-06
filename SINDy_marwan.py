import numpy as np


def sindy(X, dt, threshold=0.1):
    #Main SINDy
    pass

def afgeleide(X, dt):
    """
    Berekend afgeleide naar de tijd met numerieke differntiatie.
    """
    X_dot = np.gradient(X, dt, axis=0)

    return X_dot
