from typing import Protocol

import matplotlib.pyplot as plt

FIGSIZE = 8, 3
Z_COLOR = "tab:blue"
W_COLOR = "tab:red"
FILL_ALPHA = 0.2


class Region(Protocol):
    def plot(self, ax: plt.Axes, color: str, label: str): ...


def savefig(fig, name: str):
    fig.savefig(f"images/{name}", format="svg", bbox_inches="tight")


def get_subplots():
    return plt.subplots(
        1,
        2,
        figsize=FIGSIZE,
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )


def setup_ax(ax, label: str):
    ax.set_xlabel(f"Re(${label}$)")
    ax.set_ylabel(f"Im(${label}$)")
    ax.set_aspect("equal", "box")
    ax.axvline(color="black", linewidth=0.5)
    ax.axhline(color="black", linewidth=0.5)
    ax.grid(True, which="both", linestyle="--", color="k", alpha=FILL_ALPHA)


def z_w_plot(axs, z_region, w_region):
    setup_ax(axs[0], "z")
    z_region.plot(axs[0], Z_COLOR, "z")
    setup_ax(axs[1], "w")
    w_region.plot(axs[1], W_COLOR, "w")
