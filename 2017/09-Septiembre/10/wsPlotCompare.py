import numpy as np
import matplotlib.pyplot as plt
import os

x1_2dos,x2_2dos,l2dos,c2dos = np.loadtxt("wsPlotData_2dos.txt")
x1_3ros,x2_3ros,l3ros,c3ros = np.loadtxt("wsPlotData_3ros.txt")


plt.figure(1)
plt.plot(x1_2dos, l2dos, 'rs', label = '$l/l_0$ (2dos)')
plt.plot(x1_2dos, c2dos, 'r^', label = '$C/C_0$ (2dos)')
plt.plot(x1_3ros, l3ros, 'bs', label = '$l/l_0$ (3ros)')
plt.plot(x1_3ros, c3ros, 'b^', label = '$C/C_0$ (3ros)')
plt.legend(loc='best')
plt.xlabel('#Rewire/#Total', fontsize = 16)
plt.xscale('log',nonposx = 'clip')
plt.xlim((0.0001,1))
plt.ylim((0,1.05))
plt.savefig("wsCompare.png")

plt.figure(2)
plt.plot(x2_2dos, l2dos, 'rs', label = '$l/l_0$ (2dos)')
plt.plot(x2_2dos, c2dos, 'r^', label = '$C/C_0$ (2dos)')
plt.plot(x2_3ros, l3ros, 'bs', label = '$l/l_0$ (3ros)')
plt.plot(x2_3ros, c3ros, 'b^', label = '$C/C_0$ (3ros)')
plt.legend(loc='best')
plt.xlabel('#Rewire', fontsize = 16)
plt.xscale('log',nonposx = 'clip')
plt.ylim((0,1.05))
plt.savefig("wsCompareNotTotal.png")

plt.show()
