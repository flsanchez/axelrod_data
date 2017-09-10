import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()+'/nEdgeRew_'

nEdgeList = [0,1,5,10,49,98,249,668,1077,1435,2324]#,3368]#2500]
edgeTot = 9702
qCrit = []
qError = []

for n in nEdgeList:
	path = cwd+str(n)
	q = np.array([])
	var = np.array([])
	Smax = np.array([])
	listDir = os.listdir(path)
	aux = np.loadtxt(path+'/run.log',unpack=True)
	qError.append(aux[2])
	for files in listDir:
		if files.endswith(".txt") and files != "qlc.txt":
			filePath = path+'/'+files
			f = open(filePath,'r')
			f.readline()
			aux = f.readline()
			aux = aux.split(" ")
			n = int(aux[1])
			q = np.append(q, int(aux[3]))
			f.close()

			data = np.loadtxt(filePath,unpack=True)

			data = data[0] / n**2

			mu = np.sum(data)/np.size(data)

			Smax = np.append(Smax, mu)

			sigma2= np.sum(data*data)/np.size(data) - mu**2

			var = np.append(var, np.sqrt(sigma2))
		
	qMin = int(q[np.where(var == np.max(var))])
	qCrit.append(qMin)

x = np.array(nEdgeList,dtype='float64')/( np.array(nEdgeList) + edgeTot)
np.savetxt("qCritData_3ros.txt", [x,qCrit, qError], fmt = '%.8f', header='#Rewire/#Total qCrit qCritError')

ax=plt.axes()
ax.errorbar(x,qCrit, yerr=qError, marker='s', color='r')
ax.set_xlabel('#Rewire/#Totales')
ax.set_ylabel('q Critico')
plt.savefig('qCrit.png')
plt.show()
