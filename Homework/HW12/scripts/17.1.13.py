import matplotlib.pyplot as plt
from region import CartesianStrip


def main():
    z_region = CartesianStrip(v_min=2.0, v_max=5.0)
    w_region = z_region.map_i()

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(8, 4), sharex=True, sharey=True, constrained_layout=True
    )

    ax1.set(xlim=(-6, 6), ylim=(-6, 6))
    z_region.plot(ax1, "b", "z")
    w_region.plot(ax2, "r", "w")

    fig.savefig("images/17.1.13.svg", format="svg", bbox_inches="tight")


if __name__ == "__main__":
    main()
