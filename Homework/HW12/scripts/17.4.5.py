import numpy as np
from plot import get_subplots, savefig, z_w_plot
from region import Plane, Strip


def main():

    z_region = Strip(v_min=0, v_max=2 * np.pi)
    w_region = Plane([(0, 0)])
    fig, axs = get_subplots()

    lims = 2.1 * np.pi * np.array([-1, 1])
    axs[0].set(xlim=lims, ylim=lims)
    z_w_plot(axs, z_region, w_region)
    savefig(fig, "17.4.5.svg")


if __name__ == "__main__":
    main()
