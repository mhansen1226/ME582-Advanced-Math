from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle as Rect
from plot import FILL_ALPHA


def plot_wireframe(ax: plt.Axes, color: str, Z: np.ndarray):
    for i in range(Z.shape[0]):
        ax.plot(Z[i, :].real, Z[i, :].imag, color=color, linewidth=0.5)
    for j in range(Z.shape[1]):
        ax.plot(Z[:, j].real, Z[:, j].imag, color=color, linewidth=0.5)


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

    def plot(self, ax: plt.Axes, color: str):
        """Renders this sector onto a given matplotlib axis."""

        verts = self.get_vertices()
        ax.fill(verts.real, verts.imag, color, alpha=FILL_ALPHA)
        ax.plot(verts.real, verts.imag, color)

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

    def plot(self, ax: plt.Axes, color: str):

        if np.isfinite(self.u_min) and np.isfinite(self.u_max):
            ax.axvspan(self.u_min, self.u_max, color=color, alpha=FILL_ALPHA)
            ax.axvline(self.u_min, color=color)
            ax.axvline(self.u_max, color=color)
        elif np.isfinite(self.v_min) and np.isfinite(self.v_max):
            ax.axhspan(self.v_min, self.v_max, color=color, alpha=FILL_ALPHA)
            ax.axhline(self.v_min, color=color)
            ax.axhline(self.v_max, color=color)

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

    def plot(self, ax: plt.Axes, color: str):

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

    def plot(self, ax: plt.Axes, color: str):

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

    def plot(self, ax: plt.Axes, color: str):
        theta_outer = np.linspace(0, 2 * np.pi, 100)
        outer_circle = self.r_max * np.exp(1j * theta_outer)

        theta_inner = np.linspace(2 * np.pi, 0, 100)
        inner_circle = self.r_min * np.exp(1j * theta_inner)

        verts = np.concatenate((outer_circle, inner_circle))

        ax.fill(verts.real, verts.imag, color, alpha=FILL_ALPHA)
        ax.plot(outer_circle.real, outer_circle.imag, color)
        ax.plot(inner_circle.real, inner_circle.imag, color)


@dataclass
class SectoredAnnulus:
    r_min: float
    r_max: float
    theta_start: float
    theta_end: float

    def get_vertices(self, num_points: int = 100) -> np.ndarray:
        theta = np.linspace(self.theta_start, self.theta_end, num_points)
        arc_outer = self.r_max * np.exp(1j * theta)
        arc_inner = self.r_min * np.exp(1j * theta[::-1])  # Reversed for fill
        return np.concatenate((arc_outer, arc_inner, [arc_outer[0]]))

    def plot(self, ax: plt.Axes, color: str):
        verts = self.get_vertices()
        ax.fill(verts.real, verts.imag, color, alpha=FILL_ALPHA)
        ax.plot(verts.real, verts.imag, color)

    def map_logarithm(self) -> Rectangle:
        """Transformation: w = Ln z."""
        return Rectangle(
            u_min=np.log(self.r_min),
            u_max=np.log(self.r_max),
            v_min=self.theta_start,
            v_max=self.theta_end,
        )


@dataclass
class Rectangle:
    u_min: float
    u_max: float
    v_min: float
    v_max: float

    def plot(self, ax: plt.Axes, color: str):
        # Calculate width and height
        width = self.u_max - self.u_min
        height = self.v_max - self.v_min

        # Create and add the rectangle patch
        rect = Rect(
            (self.u_min, self.v_min),
            width,
            height,
            facecolor=color,
            alpha=FILL_ALPHA,
        )
        ax.add_patch(rect)
        ax.plot(
            [self.u_min, self.u_max, self.u_max, self.u_min, self.u_min],
            [self.v_min, self.v_min, self.v_max, self.v_max, self.v_min],
            color=color,
        )

    def map_exponential(self) -> Annulus | SectoredAnnulus:
        """Transformation: w = e^z."""
        r_min = np.exp(self.u_min)
        r_max = np.exp(self.u_max)
        if np.isclose(abs(self.v_max - self.v_min), 2 * np.pi):
            return Annulus(r_min=r_min, r_max=r_max)
        return SectoredAnnulus(
            r_min=r_min,
            r_max=r_max,
            theta_start=self.v_min,
            theta_end=self.v_max,
        )

    def fill_region(self, ax: plt.Axes, color: str, f: Callable):
        # 1. Define the grid points
        u = np.linspace(self.u_min, self.u_max, 50)
        v = np.linspace(self.v_min, self.v_max, 50)

        # 2. Extract the boundary points specifically
        # Bottom, Right, Top, Left paths
        bottom = f(u + 1j * self.v_min)
        right = f(self.u_max + 1j * v)
        top = f(np.flip(u) + 1j * self.v_max)
        left = f(self.u_min + 1j * np.flip(v))

        # 3. Concatenate into a closed loop
        boundary = np.concatenate([bottom, right, top, left])

        # 4. Fill the polygon
        ax.fill(
            boundary.real,
            boundary.imag,
            color=color,
            alpha=FILL_ALPHA,
            edgecolor="none",
        )

    def plot_wireframe(self, ax: plt.Axes, color: str, N=20):
        u = np.linspace(self.u_min, self.u_max, N)
        v = np.linspace(self.v_min, self.v_max, N)
        U, V = np.meshgrid(u, v)
        Z = U + 1j * V
        self.fill_region(ax, color, lambda z: z)
        plot_wireframe(ax, color, Z)

    def plot_mapping(self, ax: plt.Axes, color: str, f: Callable, N=20):
        # 1. Create the grid in the Z-plane (u is Re(z), v is Im(z))
        u = np.linspace(self.u_min, self.u_max, N)
        v = np.linspace(self.v_min, self.v_max, N)
        U, V = np.meshgrid(u, v)
        Z = U + 1j * V

        # 2. Apply the transformation
        W = f(Z)
        self.fill_region(ax, color, f)
        plot_wireframe(ax, color, W)


@dataclass
class Plane:
    holes: list[tuple[float, float]]

    def plot(self, ax: plt.Axes, color: str):
        ax.set_facecolor(color)
        ax.patch.set_alpha(FILL_ALPHA)
        for hole in self.holes:
            ax.plot(
                *hole,
                marker="o",
                markerfacecolor="white",
                markeredgecolor=color,
            )
