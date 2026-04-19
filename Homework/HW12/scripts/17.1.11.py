from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Sector:
    r: float
    theta_start: float
    theta_end: float

    def get_vertices(self, num_points=100) -> np.ndarray:
        """Generates closed-loop vertices (Origin -> Arc -> Origin)."""
        theta = np.linspace(self.theta_start, self.theta_end, num_points)
        arc = self.r * np.exp(1j * theta)
        return np.concatenate(([0], arc, [0]))

    def plot(self, ax: plt.Axes, color: str, label: str):
        """Renders this sector onto a given matplotlib axis."""
        verts = self.get_vertices()
        ax.fill(verts.real, verts.imag, color, alpha=0.2)
        ax.plot(verts.real, verts.imag, color)

        ax.set_xlabel(f"Re(${label}$)")
        ax.set_ylabel(f"Im(${label}$)")
        ax.set_aspect("equal", "box")
        ax.grid(True, which="both", linestyle="--", color="k", alpha=0.2)


def map_z_squared(z: Sector) -> Sector:
    return Sector(r=z.r**2, theta_start=2 * z.theta_start, theta_end=2 * z.theta_end)


def main():
    z_region = Sector(
        r=0.5,
        theta_start=-np.pi / 8,
        theta_end=np.pi / 8,
    )
    w_region = map_z_squared(z_region)

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(8, 4), sharex=True, sharey=True, constrained_layout=True
    )
    z_region.plot(ax1, "b", "z")
    w_region.plot(ax2, "r", "w")
    fig.savefig("images/17.1.11.svg", format="svg", bbox_inches="tight")


if __name__ == "__main__":
    main()
