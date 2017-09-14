import matplotlib.pyplot as plt
import sys
import numpy as np
import os

# grafica la cantidad de fragmentos que se pida en fragList en la misma figura

cwd=os.getcwd()
ls=os.listdir(cwd)

fragList = [225, 275, 325]
names = ['q_{0}.frag'.format(i) for i in fragList]
plotN = 311

for files in names:

		f = open(files,'r')
		f.readline()
		aux = f.readline()
		aux = aux.split(" ")
		n = int(aux[1])
		q = int(aux[3])
		f.close()
		plt.subplot(plotN)
		size, freq = np.loadtxt(files,unpack=True)
		plt.plot(size,freq,'ro',label="q = {0}".format(q))
		plt.yscale('log')
		plt.xscale('log')
		plt.xlabel("Fragment Size")
		plt.ylabel("Freq")
		plt.legend(loc='best')
		plotN = plotN + 1

plt.savefig("fragmentos.png")
plt.show()
