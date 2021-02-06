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

#plt.plot(Ns, list(seq1(1, N)))
for c in cs:
plt.plot(Ns, list(seq2(.4, N, cs[0])))
plt.show()