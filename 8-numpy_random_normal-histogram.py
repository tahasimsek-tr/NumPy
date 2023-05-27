# Compilerda Histogramın çizilebilmesi için gerekli kodlar:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000) #'5.0' ortalama değer, '1.0' standart sapma değeri,

plt.hist(x, 100) #'100' değeri çubuk sayısıdır.
plt.show()

# Compilerda Histogramın çizilebilmesi için gerekli kodlar:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
