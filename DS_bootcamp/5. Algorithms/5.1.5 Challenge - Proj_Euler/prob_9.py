import numpy as np

l1 = np.arange(1, 100)
l2 = np.arange(1, 100)

for i, j in zip(*l1):
	print(i, j)