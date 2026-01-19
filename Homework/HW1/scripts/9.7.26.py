import matplotlib.pyplot as plt
import numpy as np


def f(point: np.ndarray) -> np.ndarray:
    x, y, z = point
    # Add a small epsilon to x to avoid division by zero
    return x**2 + y**2 + 4 * z**2


def grad(point: np.ndarray) -> np.ndarray:
    x, y, z = point
    return np.array([2 * x, 2 * y, 8 * z])


def plot_gradient(ax, point):
    g = grad(point)
    ax.quiver(*point, *g, color="blue", normalize=True, length=0.5)


limit = 1
P = np.array([2, -1, 2])
lims = np.array([-0.5, 0.5])
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(r"$\nabla T(P)$")
plot_gradient(ax, P)
ax.set_xlim(lims + P[0])
ax.set_ylim(lims + P[1])
ax.set_zlim(lims + P[2])
ax.view_init(elev=30, azim=45)
plt.savefig("images/T_P.svg", format="svg")
plt.show()
