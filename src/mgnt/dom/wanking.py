from skimage.io import imshow
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu

from mgnt.common.plotting import plot
from mgnt.common.utils import read_columns

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


def plot_loop():
    with plot() as axes:
        axes.scatter(*list(read_columns(DOMAINS_DIR / "data.csv", [0, 1])))
