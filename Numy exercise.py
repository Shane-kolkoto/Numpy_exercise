import numpy as np
from numpy import *


x = np.arange(1, 21)
print("\nOriginal array:")
print(x)


r1 = np.mean(x)
r2 = np.average(x)
print("\nMean: ", r1)


standard_list = np.std(x)
print("\nStandard Value: : ", standard_list)

r1 = np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2)
assert np.allclose(r1, r2)
print("\nvariance: ", r1)
