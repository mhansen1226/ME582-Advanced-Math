import numpy as np
from plot import get_subplots, savefig, z_w_plot
from region import Rectangle


def main():

    z_region = Rectangle(u_min=0, u_max=1, v_min=0, v_max=np.pi)
    w_region = z_region.map_exponential()
    fig, axs = get_subplots()

    z_w_plot(axs, z_region, w_region)
    savefig(fig, "17.4.7.svg")


if __name__ == "__main__":
    main()
