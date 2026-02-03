import numpy as np
from surface import plot_surface

N = 100
u = np.linspace(0, 5, N)
v = np.linspace(0, 2 * np.pi, N)
U, V = np.meshgrid(u, v)

X = U * np.cos(V)
Y = 0.5 * U * np.sin(V)
Z = U

plot_surface(X, Y, Z, "10.5.18")
