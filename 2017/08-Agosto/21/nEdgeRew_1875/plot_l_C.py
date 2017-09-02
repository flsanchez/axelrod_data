import numpy as np
import matplotlib.pyplot as plt

q, l, c = np.loadtxt("qlc.txt")

plt.plot(q, l, 'rs', label = r'$\frac{<l>}{l_0}$')
plt.plot(q, c, 'bs', label = r'$\frac{<C>}{C_0}$')
plt.xlabel("q")
plt.ylabel(r'$\frac{<l>}{l_0} y \frac{<C>}{C_0}$')
plt.legend(loc='best')
plt.savefig("l,c_vs_q.png")
plt.show()
