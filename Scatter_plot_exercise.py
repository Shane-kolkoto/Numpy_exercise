import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
import numpy as np


temp = np.array([4.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])
sales = np.array([220, 330, 190, 340, 410, 445, 412])
temp.sort()
sales.sort()
m, b = np.polyfit(temp, sales, 1)
plt.plot(temp, m*temp + b)
plt.plot(temp, sales, 'o')
plt.scatter(temp, sales)
plt.xlabel('Temperature (degrees celcius')
plt.ylabel('Price in (R)')
plt.title('Soup sales in relation to temperature')
plt.show()
