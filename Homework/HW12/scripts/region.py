from __future__ import annotations

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

    def map_z_squared(self) -> Sector:
        return Sector(
            r=self.r**2, theta_start=2 * self.theta_start, theta_end=2 * self.theta_end
        )


@dataclass
class CartesianStrip:
    u_min: float = -np.inf
    u_max: float = np.inf
    v_min: float = -np.inf
    v_max: float = np.inf

    def plot(self, ax: plt.Axes, color: str, label: str):
        if np.isfinite(self.u_min) and np.isfinite(self.u_max):
            ax.axvspan(self.u_min, self.u_max, color=color, alpha=0.2)
            ax.axvline(self.u_min, color=color)
            ax.axvline(self.u_max, color=color)
        elif np.isfinite(self.v_min) and np.isfinite(self.v_max):
            ax.axhspan(self.v_min, self.v_max, color=color, alpha=0.2)
            ax.axhline(self.v_min, color=color)
            ax.axhline(self.v_max, color=color)

        ax.set_xlabel(f"Re(${label}$)")
        ax.set_ylabel(f"Im(${label}$)")
        ax.set_aspect("equal", "box")
        ax.grid(True, which="both", linestyle="--", color="k", alpha=0.2)

    def map_i(self) -> CartesianStrip:
        return CartesianStrip(
            u_min=-self.v_max, u_max=-self.v_min, v_min=self.u_min, v_max=self.u_max
        )
