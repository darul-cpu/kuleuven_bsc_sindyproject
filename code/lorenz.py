import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t,state,sigma=10.0,rho=28.0,beta=8.0/3.0):
  x, y, z=state
  dx=sigma*(y-x)
  dy=x*(rho-z)-y
  dz=x*y-beta*z
  return [dx,dy,dz]

def generate_lorenz_data(t_start=0.0,t_end=40.0,delta=0.01,initial_state=(1.0,1.0,1.0)):
  t=np.arrange(t_start,t_end,delta)
  oplossing= solve_ivp(lorenz,(t_start,t_end),initial_state,t_eval=t)
  X=oplossing.y.T
  return t, X
