import numpy as np

def harmonic_sum(N, precision):
  sum = np.single(0) if precision == 'single' else np.double(0)
  for k in range(1, N+1):
    sum += 1/k
  return sum

def three_sum(N, precision):
  print(N)
  sum = np.single(0) if precision == 'single' else np.double(0)
  for k in range(1, N+1):
    sum += 1/(3**k)
  return sum