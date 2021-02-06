import matplotlib.pyplot as plt
from harmonic_sum import harmonic_sum
from harmonic_sum import three_sum

def make_plot(sum_func, precision, title):
  N_list = [10**n for n in range(1, 9)]
  sums = list(map(lambda N: sum_func(N, precision), N_list))
  plt.plot(N_list, sums)
  plt.title(title)
  plt.xlabel('N')
  plt.xscale('log')
  plt.ylabel('Sum')
  plt.show()

#make_plot(harmonic_sum, "single", "Harmonic Sum Single Precision")
#make_plot(harmonic_sum, "double", "Harmonic Sum Double Precision")
make_plot(three_sum, "single", "Geometric Sum Single Precision")
#make_plot(three_sum, "double", "Geometric Sum Double Precision")