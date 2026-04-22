import numpy as np
from plot import get_subplots, savefig, wireframe
from region import Rectangle


def main():

    z_region = Rectangle(u_min=0, u_max=np.pi / 2, v_min=0, v_max=2)
    fig, axs = get_subplots()
    wireframe(axs, z_region, np.sin)
    savefig(fig, "17.4.11.svg")


if __name__ == "__main__":
    main()
