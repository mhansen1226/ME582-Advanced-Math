import matplotlib.pyplot as plt
import numpy as np

COLOR = "#03A0D5"
N = 100
x = np.linspace(0, 1, N)

fig, ax = plt.subplots(figsize=(4, 4))
ax.fill_between(x, x**2, x, color=COLOR, alpha=0.2, linewidth=2)
ax.plot(x, x, color=COLOR)
ax.plot(x, x**2, color=COLOR)
ax.spines[["right", "top"]].set_visible(False)
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.savefig("images/10.3.5.svg", format="svg")
plt.show()
