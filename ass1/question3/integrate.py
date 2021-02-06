def integrate_mp(f, M):
  h = 1/M
  return h * sum(f(k*h + h/2) for k in range(M+1))

def integrate_si(f, M):
  h = 1/M
  return (h/3) * (f(0) + 2*sum((k%2 + 1) * k*h for k in range(1, M)) + f(1))