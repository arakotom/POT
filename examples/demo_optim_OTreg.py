# -*- coding: utf-8 -*-
"""
Regularized OT with generic solver
"""

import numpy as np
import matplotlib.pylab as pl
import ot



#%% parameters

n=100 # nb bins

# bin positions
x=np.arange(n,dtype=np.float64)

# Gaussian distributions
a=ot.datasets.get_1D_gauss(n,m=20,s=20) # m= mean, s= std
b=ot.datasets.get_1D_gauss(n,m=60,s=60)

# loss matrix
M=ot.dist(x.reshape((n,1)),x.reshape((n,1)))
M/=M.max()

#%% EMD

G0=ot.emd(a,b,M)

pl.figure(3)
ot.plot.plot1D_mat(a,b,G0,'OT matrix G0')

#%% Example with Frobenisu norm regularization

def f(G): return 0.5*np.sum(G**2)
def df(G): return G

reg=1e-1
  
Gl2=ot.optim.cg(a,b,M,reg,f,df,verbose=True)

pl.figure(3)
ot.plot.plot1D_mat(a,b,Gl2,'OT matrix Frob. reg')

#%% Examlple with entropic regularization

def f(G): return np.sum(G*np.log(G))
def df(G): return np.log(G)+1
    
reg=1e-3
  
Ge=ot.optim.cg(a,b,M,reg,f,df,verbose=True)

pl.figure(4)
ot.plot.plot1D_mat(a,b,Ge,'OT matrix Entrop. reg')