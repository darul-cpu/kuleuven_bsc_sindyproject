import numpy as np

def numerieke_afgeleide(X,delta):
  X_dot=np.gradient(X,delta,axis=0)
  return X_dot
