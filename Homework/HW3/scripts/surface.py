import matplotlib.pyplot as plt
import numpy as np

STRIDE = 2
OPACITY = 0.7
CMAP = "viridis"
LINE_COLOR = "black"
LINEWIDTH = 0.5


def plot_surface(U: np.ndarray, V: np.ndarray, Z: np.ndarray, save: str):
    fig = plt.figure(figsize=(7, 6), constrained_layout=True)
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(U, V, Z, alpha=OPACITY, cmap=CMAP, edgecolor="none")

    ax.plot_wireframe(
        U,
        V,
        Z,
        rstride=STRIDE,
        cstride=STRIDE,
        color=LINE_COLOR,
        linewidth=LINEWIDTH,
        label="Parameter Curves",
    )

    # Labels and View
    ax.set_xlabel("X (u)")
    ax.set_ylabel("Y (v)")
    ax.set_zlabel("Z")
    ax.view_init(elev=30, azim=30)
    ax.legend(loc="upper center", ncol=2)
    fig.savefig(f"images/{save}.svg", format="svg")
    plt.show()
