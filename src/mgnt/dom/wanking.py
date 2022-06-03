import numpy as np
from skimage.io import imshow
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu

from mgnt.common.plotting import plot
from mgnt.common.utils import read_columns, unzip

from .currents import get_current
from .analysis import read_image, get_black_ratio
from .fs import parse_voltage, DOMAINS_DIR, get_image_path


def try_otsu(arm, voltage, thresh=None):
    img = read_image(get_image_path(arm, voltage))
    thresh = thresh or threshold_otsu(img)
    mask = img > thresh
    imshow(mask)
    plt.show()
    return mask, thresh


def save(voltage, mask):
    with open(DOMAINS_DIR / "data.csv", "a") as f:
        f.write(f"{get_current(voltage)}, {get_black_ratio(mask)}\n")


def sort_by_current(i, m):
    return unzip(sorted(zip(i, m)))


def neg(items):
    return -np.array(items)


def plot_loop():
    with plot() as axes:
        i, m = read_columns(DOMAINS_DIR / "data.csv", [0, 1])
        ia, ma = sort_by_current(i[:30], m[:30])
        ib, mb = sort_by_current(i[30:], m[30:])
        ia, ib = -np.array(ia), -np.array(ib)
        ma, mb = np.array(ma) - 0.5, np.array(mb) - 0.5
        axes.plot(ia, ma, label="a")
        axes.plot(ib, mb, label="b")
        axes.scatter(ia, ma, label="a")
        axes.scatter(ib, mb, label="b")
        axes.legend()
