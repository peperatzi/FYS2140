
from numpy import *
from matplotlib.pyplot import *


E0p = 938.27    # Rest enegy for the proton [MeV]
hbarc = 0.1973  # MeV pm
c = 3.0E2       # Speed of light [pm / as]


def Psi0(x):
    x0 = 0.100  # pm
    a = 0.005   # pm
    l = 100.0e3 # 1 / pm

    A = (1./(2*pi*a**2))**0.25
    K1 = exp(-(x-x0)**2 / (4.*a**2))
    K2 = exp(1j*l*x)

    return A * K1 * K2

def V(x):
    potential = zeros(len(x))
    potential[x<=0] = 35
    return potential

nx = 801    # Number of points in x direction
np = 1e2    # Only plot every np-th calculation (for performance)
dx = 0.001  # Distance between points

a = -0.5*nx*dx
b = 0.5*nx*dx
x = linspace(a,b,nx)

dPsidx2 = zeros(nx).astype(complex64)
Psi = Psi0(x)

T = 0.012   # How long the simulation will run
dt = 1e-7   # Distance between time steps

V_x = V(x)

ion()

figure()
line, = plot(x, abs(Psi)**2)
draw()

c1 = (1j*hbarc*c) / (2.*E0p)
c2 = -(1j*c) / hbarc


t = 0
c = 1

k1 = (1j*hbarc*c) / (2.*E0p)

while t<T:
    # Calculate the derivative
    dPsidx2[1:nx-1] = (Psi[2:nx] - 2*Psi[1:nx-1] + Psi[0:nx-2]) / dx**2

    # .. new Psi
    Psi = Psi + dt * ( c1 * dPsidx2 + c2 * V_x * Psi)

    if c==np:
        line.set_ydata(abs(Psi)**2)
        draw()
        c = 0

    t += dt
    c += 1

ioff()

show()

