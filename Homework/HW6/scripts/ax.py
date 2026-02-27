import matplotlib.pyplot as plt
from matplotlib.pyplot import Axes


def setup_axes() -> Axes:
    ax = plt.axes(xlabel="Re($z$)", ylabel="Im($z$)")
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.grid(True, linestyle=":", alpha=0.6)
    return ax
