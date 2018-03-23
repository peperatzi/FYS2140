
import numpy as np
import matplotlib.pyplot as plt

x0 = 5e-15  # m
a = 1.0
k = 1./1.38e-15

A = (1./(2*np.pi*a**2))**0.25

x = np.linspace(-5,5,1000)

psi = (A*np.exp(-(x - x0)**2/(4*a**2)))**2

plt.plot(x, psi, "b", linewidth=2)
plt.legend(["|$\Psi(x,0)|^2$",])
plt.xlabel("x")
plt.ylabel("$|\Psi(x,0)|^2$")


plt.show()
