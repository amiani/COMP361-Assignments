import math
import matplotlib.pyplot as plt

from integrate import *


Ms = [2**n for n in range(1,7)]
exact_value = 2/math.pi
def f(x):
  return math.sin(math.pi*x)
print('28: ', integrate_si(f, 48) - exact_value)


def plot_mp():
  errors = [abs(integrate_mp(f, M) - exact_value) for M in Ms]
  plt.plot(Ms, errors)
  plt.title("Midpoint Method")
  plt.xlabel("M")
  plt.ylabel("Error")
  plt.show()

def plot_si():
  errors = [abs(integrate_si(f, M) - exact_value) for M in Ms]
  plt.plot(Ms, errors)
  plt.title("Simpson's Rule")
  plt.xlabel("M")
  plt.ylabel("Error")
  plt.show()

e = 1
n = 0
while e > 10**-7:
  n += 1
  e = abs(integrate_si(f, 2**n) - exact_value)
  print(e)
print(n)

plot_mp()
#plot_si()