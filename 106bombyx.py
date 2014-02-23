import matplotlib.pyplot as plt
import numpy as np
import sys
import array

x = np.arange(1, 101)
y = [ ]
i = 0
y.insert(i,10)
i = i + 1
k = sys.argv[1]
k = float(k)

while i != 100 :
   y.insert(i, (k * float(x[i - 1])) * ((1000 - float(x[i - 1])) / 1000))
   i = i + 1

plt.plot(x,y)
plt.title("Evolution du nombre de bombyx par rapport aux generations")
plt.ylabel('Nombre de bombyx')
plt.xlabel("Generation de bombyx")
plt.show()
