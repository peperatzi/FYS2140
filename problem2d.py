
import numpy as np
import matplotlib.pyplot as plt

# Defining some constants
V_0 = 34*1e6            # eV
dx = 17*1e-15           # m
m_alpha = 3.7273*1e9    # eV*c**2
hbar = 6.5821*1e9       # eV*s

# Define a range of energies (eV)
E = np.linspace(-1e-22,1e-22, 1000)
T = 1./(1.0 + ((V_0**2)/(4*E*(V_0-E)))*np.sinh(dx*np.sqrt(2*m_alpha*(V_0-E))/hbar)**2)

# 
plt.xlabel('E')
plt.ylabel('T(E)')
plt.plot(E, T)
#plt.legend(["$\hbar=1$","$\hbar=5$","$\hbar=7$"])
plt.title("Transmision coefficient")
plt.show()


