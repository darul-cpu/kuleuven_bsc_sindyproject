import numpy as np

def poly_library(X):
  x=X[:,0] #eerste kolom
  y=X[:,1] #tweede
  z=X[:,2] #derde
  Theta=np.column_stack([np.ones(len(X)),x,y,z,x**2,x*y,x*z,y**2,y*z,z**2])
  names= ["1","x","y","z","x^2","xy","xz","y^2","yz","z^2"]
  return Theta,names
