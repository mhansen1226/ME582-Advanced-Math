import matplotlib.pyplot as plt
from sketch import circle

circle(-1, 5, 1.5, title=r"$|z + 1 - 5i| \leqq \frac{3}{2}$")
plt.savefig("images/13.3.1.svg", format="svg")
