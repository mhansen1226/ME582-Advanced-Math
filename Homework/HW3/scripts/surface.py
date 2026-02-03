import matplotlib.pyplot as plt
import numpy as np

STRIDE = 5
OPACITY = 0.7
CMAP = "viridis"
LINE_COLOR = "black"
LINEWIDTH = 0.5


def plot_surface(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, save: str, debug=False):
    fig = plt.figure(figsize=(6, 5), constrained_layout=True)
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(X, Y, Z, alpha=OPACITY, cmap=CMAP, edgecolor="none")

    ax.plot_wireframe(
        X,
        Y,
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
    if debug:
        plt.show()
    else:
        fig.savefig(f"images/{save}.svg", format="svg")
