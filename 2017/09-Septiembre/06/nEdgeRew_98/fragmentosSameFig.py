import matplotlib.pyplot as plt
import sys
import numpy as np
import os

# grafica la cantidad de fragmentos que se pida en fragList en la misma figura

cwd=os.getcwd()
ls=os.listdir(cwd)

fragList = [600, 820, 2000]

for files in ls:
	if files.endswith(".frag"):

		f = open(files,'r')
		f.readline()
		aux = f.readline()
		aux = aux.split(" ")
		n = int(aux[1])
		q = int(aux[3])
		f.close()
		if(q in fragList) :
			size, freq = np.loadtxt(files,unpack=True)
			plt.plot(np.log(size),np.log(freq),'o',label="q = {0}".format(q));
			plt.xlabel("log(frag_size)")
			plt.ylabel("log(freq)")

plt.legend(loc='best')
plt.savefig("fragmentos.png")
plt.show()
