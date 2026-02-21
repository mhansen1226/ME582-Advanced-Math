import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

PADDING_FACTOR = 1.3


def get_ax(title):
    return plt.axes(xlabel="Re($z$)", ylabel="Im($z$)", title=title)


def set_limits(ax, x, y, radius):
    padding = PADDING_FACTOR * radius
    ax.set_xlim(x - padding, x + padding)
    ax.set_ylim(y - padding, y + padding)
    ax.set_aspect("equal", adjustable="box")


def circle(x, y, radius, color="skyblue", title="", ax=None):
    if not ax:
        ax = get_ax(title)

    disk = Circle(
        (x, y),
        radius,
        edgecolor="black",
        facecolor=color,
    )
    ax.add_patch(disk)
    ax.plot(x, y, ".k")
    set_limits(ax, x, y, radius)


def donut(
    x,
    y,
    r_inner,
    r_outer,
    color="skyblue",
    title="",
    ax=None,
):
    ax = get_ax(title)
    circle(x, y, r_outer, color, title, ax)
    circle(x, y, r_inner, "white", title, ax)
    set_limits(ax, x, y, r_outer)


def wedge(
    x,
    y,
    radius,
    theta_start,
    theta_end,
    color="skyblue",
    title="",
    ax=None,
):
    if not ax:
        ax = get_ax(title)

    wedge = Wedge(
        (x, y),
        radius * 5,
        theta_start,
        theta_end,
        edgecolor="black",
        facecolor=color,
    )

    ax.add_patch(wedge)
    ax.plot(x, y, ".k")
    set_limits(ax, x, y, radius)
    return ax
