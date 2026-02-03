import numpy as np
from surface import plot_surface

N = 100
u = np.linspace(0, 2 * np.pi, N)
v = np.linspace(0, 5, N)
U, V = np.meshgrid(u, v)

X = 2 + 5 * np.cos(U)
Y = -1 + 5 * np.sin(U)
Z = V

plot_surface(X, Y, Z, "10.5.15")
