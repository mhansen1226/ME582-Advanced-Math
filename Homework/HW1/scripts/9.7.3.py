import matplotlib.pyplot as plt
import numpy as np


def f(point: np.ndarray) -> np.ndarray:
    x, y = point
    # Add a small epsilon to x to avoid division by zero
    return y / (x + 1e-9)


def grad(point: np.ndarray) -> np.ndarray:
    x, y = point
    return np.array([-y / x**2, 1 / x])


def get_mesh(limit, N):
    x = np.linspace(-limit, limit, N)
    y = np.linspace(-limit, limit, N)
    return np.meshgrid(x, y)


def plot_contours(ax, limit, cs):
    x = np.linspace(-limit, limit, 100)
    for i, c in enumerate(cs):
        ax.plot(
            x,
            c * x,
            color="black",
            linewidth=1,
            label=("Level Curves" if i == 0 else None),
        )


def plot_gradient(ax, limit, N):
    X, Y = get_mesh(limit, N)
    U, V = grad(np.array([X, Y]))
    ax.quiver(X, Y, U, V, color="blue", label=r"$\nabla f$")


limit = 1
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlabel("x")
ax.set_ylabel("y")
plot_gradient(ax, limit, 20)
plot_contours(ax, limit, [-2, -1, -1 / 2, 0, 1 / 2, 1, 2])
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_aspect("equal")
ax.legend(bbox_to_anchor=(0.5, 1.05), loc="lower center", borderaxespad=0.0, ncol=2)
plt.savefig("images/gradient_field.svg", format="svg")
plt.show()
