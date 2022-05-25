import cv2 as cv

_LOWER = (0, 0, 20)
_UPPER = (100, 100, 200)
_RED_BOUNDS = (_LOWER, _UPPER)


def otsu(image):
    return cv.threshold(cv.cvtColor(image, cv.COLOR_BGR2GRAY), 128, 192, cv.THRESH_OTSU)[1]


def red(image):
    return cv.inRange(image, *_RED_BOUNDS)
