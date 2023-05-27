import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def fonk1(x):
  return slope * x + intercept

model1 = list(map(fonk1, x))

plt.scatter(x,y)
plt.plot(x, model1)
plt.show()
  