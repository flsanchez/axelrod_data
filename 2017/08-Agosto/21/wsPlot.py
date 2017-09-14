import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()+'/nEdgeRew_'

nEdgeList = [0,1,5,10,49,97,243,625,970,1250,1875,2500]
edgeTot = 9702
l = [1]
c = [1]

for n in nEdgeList:
	if n != 0:
		path = cwd+str(n)+'/qlc.txt'
		data = np.loadtxt(path)
		l.append(np.average(data[1]))
		c.append(np.average(data[2]))

x1 = np.array(nEdgeList,dtype='float64')/edgeTot
x2 = np.array(nEdgeList)
np.savetxt("wsPlotData_2dos.txt", [x1, x2, l,c], fmt = '%.8f', header='#Rewire/#Total #Rewire l/l0 c/c0')

plt.figure(1)
plt.plot(x1, l, 'rs', label = 'l/l0')
plt.plot(x1, c, 'bs', label = 'C/C0')
plt.legend(loc='best')
plt.xlabel('#Rewire/#Total', fontsize = 16)
plt.xscale('log',nonposx = 'clip')
plt.xlim((0.0001,1))
plt.ylim((0,1.05))
plt.savefig("ws.png")

plt.figure(2)
plt.plot(x2, l, 'rs', label = 'l/l0')
plt.plot(x2, c, 'bs', label = 'C/C0')
plt.legend(loc='best')
plt.xlabel('#Rewire', fontsize = 16)
plt.xscale('log',nonposx = 'clip')
plt.ylim((0,1.05))
plt.savefig("wsNotTotal.png")

plt.show()
