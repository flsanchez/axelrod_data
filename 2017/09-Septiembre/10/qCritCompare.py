import numpy as np
import matplotlib.pyplot as plt
import os

x2dos,q2dos,qError2dos = np.loadtxt("qCritData_2dos.txt")
x3ros,q3ros,qError3ros = np.loadtxt("qCritData_3ros.txt")

ax = plt.axes()
ax.errorbar(x2dos, q2dos, yerr= qError2dos, marker ='s', color='r', label='2dos')
ax.errorbar(x3ros, q3ros, yerr= qError3ros, marker ='s', color='b', label='3ros')
ax.legend(loc='best')
ax.set_xlabel('#Rewire/#Totales')
ax.set_ylabel('q Critico')
plt.savefig('qCritCompare.png')
plt.show()
