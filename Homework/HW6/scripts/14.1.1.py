import matplotlib.pyplot as plt
import numpy as np
from ax import setup_axes

t = np.linspace(2, 5, 100)
x = t
y = t / 2

ax = setup_axes()
ax.plot(x, y)
plt.savefig("images/14.1.1.svg", format="svg")
