"""
	1000 NOKTALI BİR DAĞILIM GRAFİĞİ

"""
# Aşağıdaki ilk 3 satır histogramon çizilebilmesi için gereken kodlar:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x,y)
plt.show()

# Aşağıdaki 2 satır histogramon çizilebilmesi için gereken kodlar:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
