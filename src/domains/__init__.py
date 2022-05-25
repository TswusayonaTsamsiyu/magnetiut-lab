import cv2 as cv
import pandas as pd

from mgnt.utils import cached
from mgnt.fs import MAGNETISM_DIR

DOMAINS_DIR = MAGNETISM_DIR / "2. Domains"
IV_TABLE = DOMAINS_DIR / "VI.xlsx"

LOWER = (0, 0, 20)
UPPER = (100, 100, 200)


def is_bmp(path):
    return path.suffix == ".bmp"


def iter_images():
    return filter(is_bmp, DOMAINS_DIR.iterdir())


def get_image_path(arm, voltage):
    return DOMAINS_DIR / f"{arm}{voltage}.bmp"


def read_image(path):
    return cv.imread(str(path))


def otsu(image):
    return cv.threshold(cv.cvtColor(image, cv.COLOR_BGR2GRAY), 128, 192, cv.THRESH_OTSU)[1]


def red(image):
    return cv.inRange(image, LOWER, UPPER)


def get_black_ratio(img):
    return (img == 0).sum() / img.size


@cached
def get_iv_table():
    df = pd.read_excel(IV_TABLE)
    return dict(zip(*map(lambda i: df[i].to_numpy(), df.columns)))


def get_current(voltage):
    return get_iv_table()[abs(voltage)]


def parse_voltage(path):
    return float(path.stem[1:])


def generate_data(mask):
    for path in iter_images():
        try:
            image = read_image(path)
            yield get_current(parse_voltage(image)), get_black_ratio(mask(image))
        except KeyError:
            pass
