import numpy as np
from config import get_subplots, savefig, z_w_plot
from region import SectoredAnnulus


def main():
    z_region = SectoredAnnulus(
        r_min=1.0, r_max=4.0, theta_start=np.pi / 4, theta_end=3 * np.pi / 4
    )
    w_region = z_region.map_logarithm()
    fig, axs = get_subplots()

    z_w_plot(axs, z_region, w_region)
    savefig(fig, "17.1.19.svg")


if __name__ == "__main__":
    main()
