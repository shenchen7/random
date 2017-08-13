def clean(vec):
  x=vec[~np.isnan(vec) & ~np.isinf(vec)]
  u = np.mean(x)
  s = np.std(x)
  return np.where(np.abs(vec-u)<2*s,vec,np.nan)
  
  
  
  two python: both prive volume.
  
  
