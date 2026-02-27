import matplotlib.pyplot as plt
import numpy as np
from ax import setup_axes

t = np.linspace(0, 2, 100)
x = 1 - t
y = 1 + t

ax = setup_axes()
ax.plot(x, y)
plt.savefig("images/14.1.11.svg", format="svg")
