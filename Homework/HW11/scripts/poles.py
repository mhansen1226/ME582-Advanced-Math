import os
from typing import Callable, Iterable, Tuple

import matplotlib.pyplot as plt
import numpy as np


def get_contour_points(
    center: complex, radius: float, plane: str = "full"
) -> np.ndarray:
    """Generates the coordinates for the closed contour boundary."""
    angles = {
        "full": (0, 2 * np.pi),
        "upper": (0, np.pi),
        "lower": (np.pi, 2 * np.pi),
        "left": (0.5 * np.pi, 1.5 * np.pi),
        "right": (-0.5 * np.pi, 0.5 * np.pi),
    }
    start, end = angles.get(plane, angles["full"])
    theta = np.linspace(start, end, 500)
    arc = center + radius * (np.cos(theta) + 1j * np.sin(theta))

    # Close the shape if it's a semicircle
    return np.append(arc, arc[0]) if plane != "full" else arc


def filter_poles(
    poles: np.ndarray, center: complex, radius: float, plane: str
) -> Tuple[np.ndarray, np.ndarray]:
    """Separates poles into 'inside' and 'outside' based on distance and plane."""
    dist_mask = np.abs(poles - center) < radius

    if plane == "full":
        plane_mask = np.ones_like(poles, dtype=bool)
    elif plane == "upper":
        plane_mask = poles.imag > center.imag
    elif plane == "lower":
        plane_mask = poles.imag < center.imag
    elif plane == "left":
        plane_mask = poles.real < center.real
    elif plane == "right":
        plane_mask = poles.real > center.real
    else:
        plane_mask = np.ones_like(poles, dtype=bool)

    inside = dist_mask & plane_mask
    return poles[inside], poles[~inside]


def plot_poles(
    pole_func: Callable[[int], complex],
    n_range: Iterable[int],
    center: complex,
    radius: float,
    save_name: str,
    plane: str = "full",
):
    """Coordinates calculation, plotting, and SVG export."""
    all_poles = np.array([pole_func(n) for n in n_range], dtype=complex)
    poles_inside, poles_outside = filter_poles(all_poles, center, radius, plane)
    boundary = get_contour_points(center, radius, plane)

    fig, ax = plt.subplots(figsize=(4, 3), constrained_layout=True)
    ax.set_xlabel(r"Re($z$)")
    ax.set_ylabel(r"Im($z$)")

    ax.plot(boundary.real, boundary.imag, "b-", label=f"$C$")
    ax.fill(boundary.real, boundary.imag, "b", alpha=0.1)
    ax.plot(center.real, center.imag, "b.", markersize=4)

    # Plot Poles
    ax.scatter(
        poles_inside.real,
        poles_inside.imag,
        color="red",
        edgecolors="black",
        s=25,
        label="Inside",
        zorder=5,
    )
    ax.scatter(
        poles_outside.real,
        poles_outside.imag,
        color="gray",
        alpha=0.6,
        s=20,
        label="Outside",
    )

    # Aesthetics
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.05), ncol=3, fontsize="small")
    ax.set_aspect("equal", adjustable="datalim")

    # Export Logic
    os.makedirs("images", exist_ok=True)
    fig.savefig(f"images/{save_name}.svg", format="svg")
    plt.close(fig)

    print(f"{save_name:10} | Poles inside -> {poles_inside}")


# 16.3.15: tan(2pi z) | center 0.2, radius 0.2
plot_poles(
    pole_func=lambda n: 1 / 4 + n / 2,
    n_range=range(-1, 2),
    center=0.2 + 0j,
    radius=0.2,
    save_name="16.3.15",
)

# 16.3.17: e^z / cos(z) | center pi*i/2, radius 4.5
plot_poles(
    pole_func=lambda n: np.pi / 2 + np.pi * n,
    n_range=range(-2, 2),
    center=np.pi * 1j / 2,
    radius=4.5,
    save_name="16.3.17",
)

# 16.3.19: sinh(z) / (2z - i) | center 2i, radius 2
plot_poles(
    pole_func=lambda n: 1j / 2,
    n_range=[0],
    center=2j,
    radius=2,
    save_name="16.3.19",
)

# 16.3.21: cos(pi z) / z^5 | center 0, radius 0.5
plot_poles(
    pole_func=lambda n: 0,
    n_range=range(1),
    center=0 + 0j,
    radius=1 / 2,
    save_name="16.3.21",
)

# 16.4.1 | center 0, radius 1
k = 1.1
plot_poles(
    pole_func=lambda n: k + np.sqrt(k**2 - 1) * n,
    n_range=[-1, 1],
    center=0 + 0j,
    radius=1,
    save_name="16.4.1",
)
a = 1.1
plot_poles(
    pole_func=lambda n: (a + np.sqrt(a**2 - 1) * n) * 1j,
    n_range=[-1, 1],
    center=0 + 0j,
    radius=1,
    save_name="16.4.7",
)


plot_poles(
    pole_func=lambda n: [2 / 3, -2 / 3, 3 / 2, -3 / 2][n],
    n_range=range(4),
    center=0 + 0j,
    radius=1,
    save_name="16.4.9",
)

plot_poles(
    pole_func=lambda n: 1j * n,
    n_range=[-1, 1],
    center=0 + 0j,
    radius=1.5,
    plane="upper",
    save_name="16.4.11",
)

plot_poles(
    pole_func=lambda n: np.exp(1j * np.pi / 6 * (1 + 2 * n)),
    n_range=range(6),
    center=0 + 0j,
    radius=1.5,
    plane="upper",
    save_name="16.4.15",
)
