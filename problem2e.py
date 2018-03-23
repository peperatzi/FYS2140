
from numpy import *

hbar = 6.58e-16

def T(E, V0, m, dx):
    a = dx*sqrt(2*m*(V0-E))
    b = a/hbar
    print b
    return 1./(1 + ((V0**2)*(math.sinh(b)**2))/(4*E*(V0-E)))

print T(4.8e6, 34e6, 3.73e9, 17e-15)


