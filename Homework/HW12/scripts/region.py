from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
from config import FILL_ALPHA


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
        ax.fill(verts.real, verts.imag, color, alpha=FILL_ALPHA)
        ax.plot(verts.real, verts.imag, color)

        ax.set_xlabel(f"Re(${label}$)")
        ax.set_ylabel(f"Im(${label}$)")
        ax.set_aspect("equal", "box")
        ax.grid(True, which="both", linestyle="--", color="k", alpha=FILL_ALPHA)

    def map_z_squared(self) -> Sector:
        return Sector(
            r=self.r**2, theta_start=2 * self.theta_start, theta_end=2 * self.theta_end
        )


@dataclass
class Strip:
    u_min: float = -np.inf
    u_max: float = np.inf
    v_min: float = -np.inf
    v_max: float = np.inf

    def plot(self, ax: plt.Axes, color: str, label: str):

        if np.isfinite(self.u_min) and np.isfinite(self.u_max):
            ax.axvspan(self.u_min, self.u_max, color=color, alpha=FILL_ALPHA)
            ax.axvline(self.u_min, color=color)
            ax.axvline(self.u_max, color=color)
        elif np.isfinite(self.v_min) and np.isfinite(self.v_max):
            ax.axhspan(self.v_min, self.v_max, color=color, alpha=FILL_ALPHA)
            ax.axhline(self.v_min, color=color)
            ax.axhline(self.v_max, color=color)

        ax.set_xlabel(f"Re(${label}$)")
        ax.set_ylabel(f"Im(${label}$)")
        ax.set_aspect("equal", "box")
        ax.grid(True, which="both", linestyle="--", color="k", alpha=FILL_ALPHA)

    def map_i(self) -> Strip:
        return Strip(
            u_min=-self.v_max, u_max=-self.v_min, v_min=self.u_min, v_max=self.u_max
        )

    def map_exponential(self) -> Annulus:
        """Transformation: w = e^z. Optimized for vertical strips."""
        return Annulus(r_min=np.exp(self.u_min), r_max=np.exp(self.u_max))


@dataclass
class Circle:
    center: complex
    r: float

    def get_vertices(self, num_points: int = 100) -> np.ndarray:
        """Generates closed-loop vertices for a circle."""
        theta = np.linspace(0, 2 * np.pi, num_points)
        circle_points = self.center + self.r * np.exp(1j * theta)
        return circle_points

    def plot(self, ax: plt.Axes, color: str, label: str):

        verts = self.get_vertices()
        ax.fill(verts.real, verts.imag, color, alpha=FILL_ALPHA)
        ax.plot(verts.real, verts.imag, color)

    def map_inversion(self) -> HalfPlane:
        """Transformation: w = 1/z. Specialized for a circle passing through z=0."""
        return HalfPlane(u_min=1.0)


@dataclass
class HalfPlane:
    u_min: float = -np.inf
    u_max: float = np.inf
    v_min: float = -np.inf
    v_max: float = np.inf

    def plot(self, ax: plt.Axes, color: str, label: str):

        limit = 100  # Use a large finite value or the axis limits to prevent transform errors
        u_start = self.u_min if np.isfinite(self.u_min) else -limit
        u_end = self.u_max if np.isfinite(self.u_max) else limit
        v_start = self.v_min if np.isfinite(self.v_min) else -limit
        v_end = self.v_max if np.isfinite(self.v_max) else limit

        if np.isfinite(self.u_min) or np.isfinite(self.u_max):
            ax.axvspan(u_start, u_end, color=color, alpha=0.2)
            if np.isfinite(self.u_min):
                ax.axvline(self.u_min, color=color)
        elif np.isfinite(self.v_min) or np.isfinite(self.v_max):
            ax.axhspan(v_start, v_end, color=color, alpha=0.2)
            if np.isfinite(self.v_min):
                ax.axhline(self.v_min, color=color)


@dataclass
class Annulus:
    r_min: float
    r_max: float

    def plot(self, ax: plt.Axes, color: str, label: str):
        theta_outer = np.linspace(0, 2 * np.pi, 100)
        outer_circle = self.r_max * np.exp(1j * theta_outer)

        theta_inner = np.linspace(2 * np.pi, 0, 100)
        inner_circle = self.r_min * np.exp(1j * theta_inner)

        verts = np.concatenate((outer_circle, inner_circle))

        ax.fill(verts.real, verts.imag, color, alpha=FILL_ALPHA)
        ax.plot(outer_circle.real, outer_circle.imag, color)
        ax.plot(inner_circle.real, inner_circle.imag, color)
