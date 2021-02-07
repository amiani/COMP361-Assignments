def integrate_mp(f, M):
  h = 1/M
  return h * sum(f(k*h + h/2) for k in range(M))

def integrate_si(f, M):
  h = 1/M
  return (h/3) * (f(0) + sum(2*(k%2 + 1) * f(k*h) for k in range(1, M)) + f(1))