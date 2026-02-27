import matplotlib.pyplot as plt
import numpy as np


def plot_axlines(ax):
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)


def plot_complex_points(points):
    ax = plt.axes(xlabel="Re($z$)", ylabel="Im($z$)")
    plot_axlines(ax)

    reals = [p.real for p in points]
    imags = [p.imag for p in points]

    ax.plot(reals, imags, "r.")

    ax.grid(True, linestyle=":", alpha=0.6)


solutions = [1j * (1 + 2 * k * np.pi) for k in range(-3, 4)]
plot_complex_points(solutions)
plt.savefig("images/13.7.15.svg", format="svg")
