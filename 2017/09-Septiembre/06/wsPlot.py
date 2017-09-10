import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()+'/nEdgeRew_'

nEdgeList = [0,1,5,10,49,98,249,668,1077,1435,2324,3368]#2500]
edgeTot = 9702
l = [1]
c = [1]

for n in nEdgeList:
	if n != 0:
		path = cwd+str(n)+'/qlc.txt'
		data = np.loadtxt(path)
		l.append(np.average(data[1]))
		c.append(np.average(data[2]))

x = np.array(nEdgeList,dtype='float64')/( np.array(nEdgeList) + edgeTot)
np.savetxt("wsPlotData_3ros.txt", [x,l,c], fmt = '%.8f', header='#Rewire/#Total l/l0 c/c0')

plt.plot(x, l, 'rs', label = 'l')
plt.plot(x, c, 'bs', label = 'c')
plt.legend(loc='best')
plt.xlabel('#Rewire/#Total', fontsize = 16)
plt.xscale('log',nonposx = 'clip')
plt.xlim((0.0001,1))
plt.ylim((0,1.05))
plt.savefig("ws2.png")
plt.show()
