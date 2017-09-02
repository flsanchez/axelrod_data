import matplotlib.pyplot as plt
import sys
import numpy as np
import os

# grafica en figuras separadas todos los fragmentos de todos los directorios

ls = next(os.walk('.'))[1]
cwd = os.getcwd()
#ls = os.listdir(cwd)

for dirList in ls:
	path = cwd + "/" + dirList
	for fileName in os.listdir(path):
		if fileName.endswith(".frag"):
			pathToFile = path + '/' + fileName
			print pathToFile
			f = open(pathToFile,'r')
			f.readline()
			aux = f.readline()
			aux = aux.split(" ")
			n = int(aux[1])
			q = int(aux[3])
			f.close()
			#if(q == int(sys.argv[1])) :
			size, freq = np.loadtxt(pathToFile,unpack=True)
			#bins = np.arange(0,n**2,n**2/10.0)
			#plt.hist(freq, bins = bins)
			#plt.bar(size,freq)
			plt.plot(size,freq,'ro')
			#plt.xlim((-10,2510))
			plt.xscale('log')
			plt.yscale('log')
			plt.xlabel("Fragment Size")
			plt.ylabel("Freq")
			plt.title("Distribucion de fragmentos para q = {0}".format(q))
			plt.savefig(path+"/fragDist_q_{0}.png".format(q))
			#plt.show()			
			plt.clf()
			
