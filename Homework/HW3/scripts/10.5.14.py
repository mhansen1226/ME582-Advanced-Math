import numpy as np
from surface import plot_surface


def get_z(x, y):
    return (12 - 4 * x - 3 * y) / 2


x = np.linspace(0, 3, 20)
y = np.linspace(0, 4, 20)
U, V = np.meshgrid(x, y)
Z = get_z(U, V)

plot_surface(U, V, Z, "10.5.14")
