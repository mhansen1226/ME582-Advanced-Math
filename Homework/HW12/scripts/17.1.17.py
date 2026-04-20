import numpy as np
from config import get_subplots, savefig, z_w_plot
from region import Strip


def main():
    z_region = Strip(u_min=np.log(2), u_max=np.log(4))
    w_region = z_region.map_exponential()

    fig, axs = get_subplots()

    z_w_plot(axs, z_region, w_region)
    savefig(fig, "17.1.17.svg")


if __name__ == "__main__":
    main()
