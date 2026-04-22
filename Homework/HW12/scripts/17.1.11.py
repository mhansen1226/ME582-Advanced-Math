import numpy as np
from plot import get_subplots, savefig, z_w_plot
from region import Sector


def main():
    z_region = Sector(
        r=0.5,
        theta_start=-np.pi / 8,
        theta_end=np.pi / 8,
    )
    w_region = z_region.map_z_squared()

    fig, axs = get_subplots()
    z_w_plot(axs, z_region, w_region)
    savefig(fig, "17.1.11.svg")


if __name__ == "__main__":
    main()
