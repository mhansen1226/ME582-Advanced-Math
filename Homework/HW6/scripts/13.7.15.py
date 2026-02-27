import matplotlib.pyplot as plt
import numpy as np
from ax import setup_axes


def plot_complex_points(points):
    ax = setup_axes()

    reals = [p.real for p in points]
    imags = [p.imag for p in points]

    ax.plot(reals, imags, "r.")


solutions = [1j * (1 + 2 * k * np.pi) for k in range(-3, 4)]
plot_complex_points(solutions)
plt.savefig("images/13.7.15.svg", format="svg")
