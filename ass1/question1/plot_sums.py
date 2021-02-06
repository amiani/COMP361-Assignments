import matplotlib.pyplot as plt
from harmonic_sum import harmonic_sum
from harmonic_sum import three_sum

def make_plot(sum_func, precision):
  N_list = [10**n for n in range(9)]
  sums = list(map(lambda N: sum_func(N, precision), N_list))
  fig = plt.plot(N_list, sums)
  plt.show()

make_plot(harmonic_sum, "single")
make_plot(harmonic_sum, "double")
make_plot(three_sum, "single")
make_plot(three_sum, "double")