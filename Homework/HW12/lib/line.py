from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class LineSegment:
    x_const: float
    y_start: float
    y_end: float

    def get_points(self, num_points: int = 200) -> np.ndarray:
        """Generates points along the line segment z = x_const + iy."""
        y = np.linspace(self.y_start, self.y_end, num_points)
        return self.x_const + 1j * y

    def plot(self, ax: plt.Axes, color: str):
        """Renders the line segment curve onto a given matplotlib axis."""
        points = self.get_points()
        ax.plot(
            points.real,
            points.imag,
            color=color,
        )

    def map_exponential(self) -> CircleCurve:
        """Transformation: w = e^z. Optimized for vertical segments."""
        return CircleCurve(r=np.exp(self.x_const), center=0j)


@dataclass
class CircleCurve:
    r: float
    center: complex = 0j

    def get_points(self, num_points: int = 200) -> np.ndarray:
        """Generates points along the circle w = center + r * exp(it)."""
        theta = np.linspace(-np.pi, np.pi, num_points)
        return self.center + self.r * np.exp(1j * theta)

    def plot(self, ax: plt.Axes, color: str):
        """Renders the circular curve onto a given matplotlib axis."""
        points = self.get_points()
        ax.plot(points.real, points.imag, color=color)
