import cv2 as cv

from .currents import get_current
from .fs import iter_images, parse_voltage


def read_image(path):
    return cv.imread(str(path))


def get_black_ratio(img):
    return (img == 0).sum() / img.size


def generate_data(mask):
    for path in iter_images():
        try:
            image = read_image(path)
            yield get_current(parse_voltage(image)), get_black_ratio(mask(image))
        except KeyError:
            pass
