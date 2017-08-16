def clean(vec):
  x=vec[~np.isnan(vec) & ~np.isinf(vec)]
  u = np.mean(x)
  s = np.std(x)
  return np.where(np.abs(vec-u)<2*s,vec,np.nan)
  
  
  
  two python: both prive volume.
#import scipy as sp
#import numpy as np
#import scipy.stats as ss
#delay=DELAY
##dr is the Data Registry
#valid = dr.GetData("UNIVID")
#Lines above will be added as a common header to your code, without "#".
# -------------------------Write your code below------------------------


#load dataset
eps_offset = dr.GetData('etv_eps_offset')
eps_dir = dr.GetData('etv_eps_est_dir')
eps_prev = dr.GetData('etv_eps_prev_est')
ntprft = dr.GetData('etv_ntprft_estimate')
ntprft_prev = dr.GetData('etv_ntprft_prev_est')
close = dr.GetData("close")
ndays=10
prealphas = np.zeros(close.shape[1])

def Generate(di,alpha):
  global prealphas,ndays
  if ndays == 10:
    ndays= 1
    for ii in range(len(alpha)):
      alpha[ii] = np.nan
      start, num = eps_offset[di][ii]
      if start >=0 and num>0:
        array =[]
        array[:] = eps_dir[start:start+num]
        n1up = array.count("U")
        n1dw = num-n1up
        #n2up = np.sum(ntprft[start:start+num]>ntprft_prev[start:start+num])
        #n2dw = np.sum(ntprft[start:start+num]<=ntprft_prev[start:start+num])

        if n1up+n1dw >0:
          alpha[ii] = (1.0*(n1up )/(n1up+n1dw ))#
      alpha[:]=where(valid[di,:],alpha[:],np.nan)
      prealphas[:] = alpha[:]
  else:
    alpha[:]=prealphas[:]
    ndays = ndays + 1






#Python code is copyright © 2001-2014 Python Software Foundation. All Rights Reserved

