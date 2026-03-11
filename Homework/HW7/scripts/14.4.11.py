import matplotlib.pyplot as plt
import numpy as np

center_x, center_y = 0, 1
radius = 2
theta = np.linspace(0, 2 * np.pi, 500)

x_circle = center_x + radius * np.cos(theta)
y_circle = center_y + radius * np.sin(theta)

pole_x, pole_y = 0.5, 0

# 3. Create the Plot
fig, ax = plt.subplots()

# Plot the axes
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

# Plot the contour C
ax.plot(x_circle, y_circle, color="blue")
ax.fill(x_circle, y_circle, color="blue", alpha=0.1)

# Plot the singularity point
ax.scatter(pole_x, pole_y, color="red", marker="x", label=r"$z_0$")

ax.set_aspect("equal")
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.grid(True, linestyle=":", alpha=0.7)
ax.legend(loc="upper right")

plt.savefig("images/14.4.11.svg", format="svg")
plt.show()
