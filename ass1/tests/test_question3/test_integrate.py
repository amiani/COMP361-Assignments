from question3.integrate import integrate_mp
from question3.integrate import integrate_si

def linear(x):
  return x

def test_integrate_mp():
  assert integrate_mp(linear, 1) == 2
  assert integrate_mp(linear, 3) == (1/3) * (1/6 + 3/6 + 5/6 + 7/6)

def test_integrate_si():
 assert integrate_si(linear, 1) == (1/3) * (0 + 1)
 assert integrate_si(linear, 4) == (1/12) * (0 + 1 + 1 + 3 + 1)