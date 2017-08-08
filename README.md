## News return
Trading hours: News return is the 15-minute return over the same period that the news occurs.
Holiday etc: Nearest subsequent overnight return


Xbool = X[np.all(isfinite(X), axis=1)]
#X = X[Xbool,:]
X[~Xbool,:] = 0

Ybool = Y[np.all(isfinite(Y), axis=1)]
#Y = Y[Xbool,:]
X[~Xbool,:] = 0
