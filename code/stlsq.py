import numpy as np

def stlsq(Theta,X_dot,threshold=0.1,iteration=10):
  Xi=np.linlang.lstsq(Theta,X_dot,rcond=None)[0]
  for i in range(iteration):
    small=np.abs(Xi)<threshold
    Xi[small]=0.0
    for k in range(X_dot.shape[1]):
      active= ~small[:,k]#welke termen blijven nog over ?
      if np.any(active):
        Xi[active,k]=np.linalg.lstsq(Theta[:,active],X_dot[:k],rcond=None)[0]
    return Xi
