import numpy as np
from plot import get_subplots, savefig, wireframe
from region import Rectangle


def plot(ax, N=9):
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.cos(X + 1j * Y)
    ax.plot_surface(X, Y, Z.real, cmap="viridis")
    ax.plot_surface(X, Y, Z.imag, cmap="plasma")


def main():

    z_region = Rectangle(u_min=-2, u_max=2, v_min=-2, v_max=2)
    fig, axs = get_subplots()
    wireframe(axs, z_region, np.cos)
    savefig(fig, "17.4.19.svg")


if __name__ == "__main__":
    main()
