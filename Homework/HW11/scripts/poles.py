import os
from typing import Callable, Iterable, Tuple

import matplotlib.pyplot as plt
import numpy as np

# --- Boundary Generation ---


def get_circle_points(center: complex, radius: float) -> np.ndarray:
    """Coordinates for a full closed circle."""
    theta = np.linspace(0, 2 * np.pi, 500)
    return center + radius * (np.cos(theta) + 1j * np.sin(theta))


def get_uhp_points(center: complex, radius: float) -> np.ndarray:
    """Coordinates for the UHP boundary (Arc + Real Segment)."""
    theta = np.linspace(0, np.pi, 500)
    arc = center + radius * (np.cos(theta) + 1j * np.sin(theta))
    return np.append(arc, arc[0])


# --- Filtering Logic ---


def filter_poles(poles: np.ndarray, center: complex, radius: float, mode: str):
    """Separates poles into Inside, Outside, and Real Zeros (for UHP)."""
    dist_mask = np.abs(poles - center) < radius

    if mode == "uhp":
        # Check for poles sitting on the real axis (relative to center)
        real_axis_mask = np.abs(poles.imag - center.imag) < 1e-9
        upper_mask = (poles.imag - center.imag) > 1e-9

        inside = dist_mask & upper_mask
        on_axis = dist_mask & real_axis_mask
        outside = ~(inside | on_axis)
        return poles[inside], poles[outside], poles[on_axis]
    else:
        inside = dist_mask
        return poles[inside], poles[~inside], np.array([])


def plot_points(ax, points, color, label):
    if len(points) == 0:
        return
    ax.scatter(
        points.real,
        points.imag,
        color=color,
        edgecolors="black",
        s=30,
        label=label,
        zorder=5,
    )


def plot_poles(
    pole_func: Callable[[int], complex],
    n_range: Iterable[int],
    center: complex,
    radius: float,
    save_name: str,
    mode: str = "circle",
):
    """Calculates, filters, and generates SVG plots."""
    all_poles = np.array([pole_func(n) for n in n_range], dtype=complex)
    inside, outside, real_zeros = filter_poles(all_poles, center, radius, mode)

    boundary = (
        get_uhp_points(center, radius)
        if mode == "uhp"
        else get_circle_points(center, radius)
    )

    fig, ax = plt.subplots(figsize=(4.5, 3.5), constrained_layout=True)
    ax.set_xlabel(r"Re($z$)")
    ax.set_ylabel(r"Im($z$)")

    # Plot Contour
    ax.plot(boundary.real, boundary.imag, "b-", lw=1.2, label="Contour")
    ax.fill(boundary.real, boundary.imag, "b", alpha=0.1)

    # Plot Poles
    plot_points(ax, inside, "red", "Inside")
    plot_points(ax, real_zeros, "gold", "Real")
    plot_points(ax, outside, "gray", "Outside")

    ax.axhline(center.imag, color="black", lw=0.8)
    ax.axvline(center.real, color="black", lw=0.8)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(
        loc="lower center", bbox_to_anchor=(0.5, 1.05), ncol=4, fontsize="x-small"
    )
    ax.set_aspect("equal", adjustable="datalim")

    os.makedirs("images", exist_ok=True)
    fig.savefig(f"images/{save_name}.svg", format="svg")
    plt.close(fig)
    print(
        f"{save_name:10} | Mode: {mode:6} | Inside: {len(inside)} | Real Zeros: {len(real_zeros)}"
    )


# --- Execution of All Current Plots ---

plot_poles(
    lambda n: 1 / 4 + n / 2,
    range(-1, 2),
    0.2 + 0j,
    0.2,
    "16.3.15",
)
plot_poles(
    lambda n: np.pi / 2 + np.pi * n,
    range(-2, 2),
    np.pi * 1j / 2,
    4.5,
    "16.3.17",
)
plot_poles(
    lambda n: 1j / 2,
    [0],
    2j,
    2,
    "16.3.19",
)
plot_poles(
    lambda n: 0,
    range(1),
    0j,
    0.5,
    "16.3.21",
)
k = 1.1
plot_poles(
    lambda n: k + np.sqrt(k**2 - 1) * n,
    [-1, 1],
    0j,
    1,
    "16.4.1",
)
a = 1.1
plot_poles(
    lambda n: (a + np.sqrt(a**2 - 1) * n) * 1j,
    [-1, 1],
    0j,
    1,
    "16.4.7",
)
plot_poles(
    lambda n: [2 / 3, -2 / 3, 3 / 2, -3 / 2][n],
    range(4),
    0j,
    1,
    "16.4.9",
)
plot_poles(
    lambda n: 1j * n,
    [-1, 1],
    0j,
    1.5,
    "16.4.11",
    "uhp",
)
plot_poles(
    lambda n: np.exp(1j * np.pi / 6 * (1 + 2 * n)),
    range(6),
    0j,
    1.5,
    "16.4.15",
    "uhp",
)
plot_poles(
    lambda n: [1, 2j, -2j][n],
    range(3),
    0j,
    2.5,
    "16.4.21",
    "uhp",
)
plot_poles(
    lambda n: n,
    range(-1, 2),
    0j,
    1.5,
    "16.4.25",
    "uhp",
)
