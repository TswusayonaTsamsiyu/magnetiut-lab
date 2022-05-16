import numpy as np


def get_max(array: np.ndarray):
    max_value = np.max(array)
    return max_value, get_index(array, max_value)


def get_index(array: np.ndarray, value):
    return np.where(array == value)[0][0]


def finde_die_spitze(measurement) -> tuple[float, float]:
    max_x, max_index = get_max(measurement.Vr)
    return max_x, measurement.Vc[max_index]


def unzip(tuples):
    return zip(*tuples)


def to_csv(measurement):
    return "\n".join(map(lambda t: f"{t[0]}, {t[1]}", zip(measurement.Vr, measurement.Vc)))
