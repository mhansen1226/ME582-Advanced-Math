from plot import get_subplots, savefig, z_w_plot
from region import Strip


def main():
    z_region = Strip(v_min=2.0, v_max=5.0)
    w_region = z_region.map_i()

    fig, axs = get_subplots()

    axs[0].set(xlim=(-6, 6), ylim=(-6, 6))
    z_w_plot(axs, z_region, w_region)

    savefig(fig, "17.1.13.svg")


if __name__ == "__main__":
    main()
