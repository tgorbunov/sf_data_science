import numpy as np

def get_unique_loto(num):
  loto = np.random.randint(1, 101, size=(num, 5, 5))
  for i in range(num):
    loto_5_5 = np.random.choice(101, size=(5, 5), replace=False)
    loto[i] = loto_5_5
  return loto

print(get_unique_loto(10))