import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 1.5, 100)
y = np.arccos(np.exp(1 - x) * np.cos(1))

fig, ax = plt.subplots(figsize=(4, 4))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Level Curve")
plt.grid(True)
plt.savefig("images/level_curve.svg", format="svg")
plt.show()
