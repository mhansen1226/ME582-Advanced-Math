from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


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


def map_multiply_by_i(z: CartesianStrip) -> CartesianStrip:
    return CartesianStrip(u_min=-z.v_max, u_max=-z.v_min, v_min=z.u_min, v_max=z.u_max)


def main():
    z_region = CartesianStrip(v_min=2.0, v_max=5.0)
    w_region = map_multiply_by_i(z_region)

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(8, 4), sharex=True, sharey=True, constrained_layout=True
    )

    ax1.set(xlim=(-6, 6), ylim=(-6, 6))
    z_region.plot(ax1, "b", "z")
    w_region.plot(ax2, "r", "w")

    fig.savefig("images/17.1.13.svg", format="svg", bbox_inches="tight")


if __name__ == "__main__":
    main()
