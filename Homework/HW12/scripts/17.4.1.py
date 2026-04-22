import numpy as np
from config import get_subplots, savefig, z_w_plot
from line import LineSegment


def main():
    c_val = np.log(2.0)
    z_curve = LineSegment(x_const=c_val, y_start=-np.pi, y_end=np.pi)
    w_curve = z_curve.map_exponential()
    fig, axs = get_subplots()

    z_w_plot(axs, z_curve, w_curve)
    savefig(fig, "17.4.1.svg")


if __name__ == "__main__":
    main()
