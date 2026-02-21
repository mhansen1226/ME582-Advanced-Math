import matplotlib.pyplot as plt
from sketch import wedge

theta = 90
wedge(-1, 0, 1, -theta, theta, title=r"Re $z \geqq -1$")
plt.savefig("images/13.3.7.svg", format="svg")
