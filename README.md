## News return
Trading hours: News return is the 15-minute return over the same period that the news occurs.
Holiday etc: Nearest subsequent overnight return


Xbool = X[np.all(isfinite(X), axis=1)]
#X = X[Xbool,:]
X[~Xbool,:] = 0

Ybool = Y[np.all(isfinite(Y), axis=1)]
#Y = Y[Xbool,:]
X[~Xbool,:] = 0



#import scipy as sp
#import numpy as np
#import scipy.stats as ss
#delay=DELAY
##dr is the Data Registry
#valid = dr.GetData("UNIVID")
#Lines above will be added as a common header to your code, without "#".
# -------------------------Write your code below------------------------

from sklearn import svm
import pandas as pd
from sklearn import linear_model
from sklearn import svm

close = dr.GetData("close")
vwap = dr.GetData("vwap")
returns = dr.GetData("returns")
#volume = dr.GetData("volume")
eps = dr.GetData("eps")

#ebitda = dr.GetData("EBITDA")
eps = dr.GetData("eps")
#bs = dr.GetData("bookvalue_ps")

close = dr.GetData("close")
vwap = dr.GetData("vwap")
returns = dr.GetData("returns")
volume = dr.GetData("volume")
eps = dr.GetData("eps")
sharesout = dr.GetData("sharesout")

ndays = 250
prealphas = np.zeros(close.shape[1])
#fuck nans
def fucknans(array):
    df=pd.DataFrame(array)
    df1 = df.fillna(method="ffill")
    dfc = df1.fillna(method="bfill")
    result = dfc.values
    return result
  
  
  
def fuckinf(alpha):
  x=np.zeros(close.shape[1])
  x[:]=alpha[:]
  x[np.isinf(x)]=np.nan
  return x
  
def Generate(di,alpha):
    global ndays,prealphas
    if ndays == 250:
      ndays = 1
      momen1 = fucknans(close[di-delay-1,:])/fucknans(vwap[di-delay-1,:])
      feat1 = np.array(momen1)
      feat2 = np.array([eps[di-delay-1,:]]).T
      feat3 = np.array([eps[di-delay-1,:]]).T
      rawdata = np.append(feat1,feat2,axis=1)
      rawdata1 = np.append(rawdata,feat3,axis = 1)
      x_train = fucknans(rawdata)
      momen2 = fucknans(close[di-delay,:])/fucknans(vwap[di-delay,:])
      featn1 = np.array(momen2)
      featn2 = np.array([eps[di-delay,:]]).T
      featn3 = np.array([eps[di-delay,:]]).T
      rawdata_n = np.append(featn1,featn2,axis=1)
      rawdata_n1 = np.append(rawdata_n,featn3,axis = 1)
      x_test = fucknans(rawdata_n)
      y_train = fucknans(np.array([returns[di-delay,:]]).T)
      #reg = linear_model.Lasso(alpha = 0.1)
      reg = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)
      reg.fit(x_train,y_train)
      rawpre = reg.predict(x_test)
      pre = np.array([rawpre]).T
      fuck = fuckinf(pre[:,0])
      alpha[:] = fuck
      prealphas[:]=pre[:,0]
    else:
      alpha[:]=prealphas[:]
      ndays=ndays+1

#Python code is copyright © 2001-2014 Python Software Foundation. All Rights Reserved
