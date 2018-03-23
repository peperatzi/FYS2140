
import numpy as np
import matplotlib.pyplot as plt

x0 = 5e-15  # m
a = 1.0
k = 1./1.38e-15

A = (1./(2*np.pi*a**2))**0.25

x = np.linspace(0,5e-14,1000)

psi = A*np.exp(-(x - x0)**2/(4*a**2))*np.exp(1j*k*x)

plt.plot(x, psi, "b", linewidth=2)
xpos = 0.865e-14
ypos = 0.62
plt.plot([xpos,xpos], [-0.8,1.0], "--k",)
plt.plot([xpos,xpos], [ypos,ypos], "or", linewidth=1)
plt.legend(["$\Psi(x,0)$", "Wavelength indication"])
plt.xlabel("x")
plt.ylabel("$|\Psi(x,0)|^2$")


plt.show()
