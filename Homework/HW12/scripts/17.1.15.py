from config import get_subplots, savefig, z_w_plot
from region import Circle


def main():
    z_region = Circle(center=0.5 + 0j, r=0.5)
    w_region = z_region.map_inversion()

    fig, axs = get_subplots()

    axs[0].set(xlim=(-1, 3), ylim=(-2, 2))
    z_w_plot(axs, z_region, w_region)
    savefig(fig, "17.1.15.svg")


if __name__ == "__main__":
    main()
