import matplotlib.pyplot as plt
import sys
import numpy as np
import os

# grafica en figuras separadas todos los fragmentos

cwd=os.getcwd()
ls=os.listdir(cwd)

for files in ls:
	if files.endswith(".frag"):

		f = open(files,'r')
		f.readline()
		aux = f.readline()
		aux = aux.split(" ")
		n = int(aux[1])
		q = int(aux[3])
		f.close()
		#if(q == int(sys.argv[1])) :
		size, freq = np.loadtxt(files,unpack=True)
		
		plt.plot(size,freq,'ro')
		plt.xlim((-10,2510))
		plt.yscale('log')
		plt.xlabel("Fragment Size")
		plt.ylabel("Freq")
		plt.title("Distribucion de fragmentos para q = {0}".format(q))
		plt.savefig(cwd+"/frag/fragDist_q_{0}.png".format(q))
		plt.clf()
#plt.show()
