from question1.harmonic_sum import harmonic_sum
from question1.harmonic_sum import three_sum

def test_harmonic_sum():
  assert harmonic_sum(1, "single") == 1
  assert harmonic_sum(1, 'double') == 1
  assert harmonic_sum(5, "single") == 1 + 1/2 + 1/3 + 1/4 + 1/5

def test_three_sum():
  assert three_sum(1, "single") == 1/3
  assert three_sum(1, 'double') == 1/3
  assert three_sum(5, "single") == 1/3 + 1/9 + 1/27 + 1/81 + 1/243