import matplotlib.pyplot as plt

def seq1(x0, N):
  yield x0
  x = x0
  for i in range(N-1):
    x = (2*x**3 + 5) / (3*x**2)
    yield x

cs = [.95, 1.55, 2, 3.6, 3.98]
def seq2(x0, N, c):
  yield x0
  x = x0
  for i in range(N-1):
    x = c*x*(1-x)
    yield x

N = 20
Ns = [x+1 for x in range(N)]

def plot_seq1():
  plt.plot(Ns, list(seq1(1, N)))
  plt.title(r'Behaviour of $\frac{2x^3+5}{3x^2}$')
  plt.xlabel("k")
  plt.ylabel("$x^{(k)}$")
  plt.show()

#plot_seq1()
def plot_seq2():
  plt.title(r'Behaviour of logistic equation')
  for c in cs:
    plt.plot(Ns, list(seq2(.1, N, c)))
  plt.xlabel('k')
  plt.ylabel('$x^{(k)}$')
  plt.legend(title='c values', labels=cs)
  plt.show()

plot_seq2()