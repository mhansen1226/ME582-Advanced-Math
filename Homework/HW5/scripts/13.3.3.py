import matplotlib.pyplot as plt
import numpy as np
from sketch import donut

donut(4, -2, np.pi, 3 * np.pi, title=r"$\pi < |z - 4 + 2i| < 3\pi$")
plt.savefig("images/13.3.3.svg", format="svg")
