import matplotlib.pyplot as plt
import numpy as np
from sketch import wedge

theta = np.rad2deg(np.pi / 4)
wedge(0, 0, 1, -theta, theta, title=r"$|\arg z| < \frac{1}{4}\pi$")
plt.savefig("images/13.3.5.svg", format="svg")
