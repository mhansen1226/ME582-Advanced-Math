import numpy as np
from plot import get_subplots, savefig, wireframe
from region import Rectangle


def main():

    z_region = Rectangle(u_min=0, u_max=2 * np.pi, v_min=1, v_max=3)
    fig, axs = get_subplots()
    wireframe(axs, z_region, np.sin)
    savefig(fig, "17.4.13.svg")


if __name__ == "__main__":
    main()
