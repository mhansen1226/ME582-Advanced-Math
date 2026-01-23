import matplotlib.pyplot as plt
import numpy as np


def plot_volume(ax, N=500):
    x = np.linspace(0, 1, N)
    y = np.linspace(0, 1, N)
    z = np.linspace(0, 1, N)

    X, Y = np.meshgrid(x, y)
    Z = 1 - X**2

    mask = Y <= 1 - X**2
    surface(ax, X, Y, np.where(mask, Z, np.nan))

    X, Z = np.meshgrid(x, z)
    Y2 = 1 - X**2
    mask2 = Z <= 1 - X**2
    surface(ax, X, np.where(mask2, Y2, np.nan), Z)


def surface(ax, X, Y, Z, color="#03A0D5", alpha=0.5):
    ax.plot_surface(X, Y, Z, linewidth=0, color=color, alpha=alpha)


def plot_wireframe(ax, color="#03A0D5", width=1):
    t = np.linspace(0, 1, 100)

    # --- Edges on the Coordinate Axes ---
    ax.plot(t, 0 * t, 0 * t, color=color, linewidth=width)
    ax.plot(0 * t, t, 0 * t, color=color, linewidth=width)
    ax.plot(0 * t, 0 * t, t, color=color, linewidth=width)

    # --- Edges on the Coordinate Planes ---
    ax.plot(t, 1 - t**2, 0 * t, color=color, linewidth=width)
    ax.plot(t, 0 * t, 1 - t**2, color=color, linewidth=width)

    # --- Edges on the Back Face (x=0) ---
    ax.plot(0 * t, 1 + 0 * t, t, color=color, linewidth=width)
    ax.plot(0 * t, t, 1 + 0 * t, color=color, linewidth=width)

    # --- The Intersection Ridge ---
    # Where y = 1 - x^2 and z = 1 - x^2 meet
    ax.plot(t, 1 - t**2, 1 - t**2, color=color, linewidth=width)


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.grid(False)
ax.view_init(elev=25, azim=45)
plot_volume(ax)
plot_wireframe(ax)
fig.savefig("images/10.3.10.svg", format="svg")
plt.show()
