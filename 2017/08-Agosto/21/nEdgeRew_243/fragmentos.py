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
		
		plt.plot(np.log(size),np.log(freq),'ro');
		plt.xlabel("log(frag_size)")
		plt.ylabel("log(freq)")
		plt.title("Distribucion de fragmentos para q = {0}".format(q))
		plt.savefig("fragDist_q_{0}".format(q))
		plt.clf()
#plt.show()
