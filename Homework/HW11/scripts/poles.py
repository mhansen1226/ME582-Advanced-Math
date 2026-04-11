from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def plot_poles(
    pole_func: Callable[[int], complex],
    n_range: range,
    center: complex,
    radius: float,
    save_name: str,
):
    all_poles = np.array([pole_func(n) for n in n_range], dtype=complex)

    distances = np.abs(all_poles - center)
    inside_mask = distances < radius

    poles_inside = all_poles[inside_mask]
    poles_outside = all_poles[~inside_mask]

    fig = plt.figure(constrained_layout=True)
    ax = plt.axes(xlabel=r"Re($z$)", ylabel=r"Im($z$)")

    theta = np.linspace(0, 2 * np.pi, 500)
    circle = center + radius * (np.cos(theta) + 1j * np.sin(theta))
    ax.plot(circle.real, circle.imag, "b-", label="$C$")
    ax.fill(circle.real, circle.imag, "b", alpha=0.1)
    ax.plot(center.real, center.imag, "b.")

    ax.scatter(
        poles_inside.real,
        poles_inside.imag,
        color="red",
        edgecolors="black",
        s=20,
        label="Poles Inside",
        zorder=5,
    )
    ax.scatter(
        poles_outside.real,
        poles_outside.imag,
        color="gray",
        alpha=0.7,
        s=20,
        label="Poles Outside",
    )

    ax.axhline(0, color="black", lw=1)
    ax.axvline(0, color="black", lw=1)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    ax.set_aspect("equal", adjustable="datalim")
    fig.savefig(f"images/{save_name}.svg", format="svg")
    print(f"{save_name}: poles inside -> {poles_inside}")


plot_poles(
    pole_func=lambda n: 1 / 4 + n / 2,
    n_range=range(-1, 2),
    center=0.2 + 0j,
    radius=0.2,
    save_name="16.3.15",
)
plot_poles(
    pole_func=lambda n: np.pi / 2 + np.pi * n,
    n_range=range(-2, 2),
    center=np.pi * 1j / 2,
    radius=4.5,
    save_name="16.3.17",
)
