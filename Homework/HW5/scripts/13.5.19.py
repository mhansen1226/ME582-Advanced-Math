import matplotlib.pyplot as plt
import numpy as np


def plot_complex_points(points, title=""):
    ax = plt.axes(xlabel="Re($z$)", ylabel="Im($z$)", title=title)

    reals = [p.real for p in points]
    imags = [p.imag for p in points]

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")
    ax.plot(reals, imags, "ro", markersize=8, label=r"$z = 2k\pi i$")

    ax.grid(True, linestyle=":", alpha=0.6)
    plt.legend()


solutions = [2 * k * np.pi * 1j for k in range(-3, 4)]
plot_complex_points(solutions, title="$e^z = 1$")
plt.savefig("images/13.5.19.svg", format="svg")
