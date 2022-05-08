import numpy as np


def get_max(array: np.ndarray):
    max_value = np.max(array)
    return max_value, np.where(array == max_value)[0][0]


def finde_die_spitze(measurement) -> tuple[float, float]:
    max_x, max_index = get_max(measurement.Vr)
    return max_x, measurement.Vc[max_index]


def unzip(tuples):
    return zip(*tuples)
