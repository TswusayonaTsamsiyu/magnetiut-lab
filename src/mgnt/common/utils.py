import numpy as np
import pandas as pd
from pathlib import Path
from functools import lru_cache

cached = lru_cache(None)


def get_extrema(array: np.ndarray):
    max_value = np.max(array)
    min_value = np.min(array)
    return max_value, get_index(array, max_value), min_value, get_index(array, min_value)


def get_index(array: np.ndarray, value):
    return np.where(array == value)[0][0]


def unzip(tuples):
    return zip(*tuples)


def read_columns(path: Path, columns: list[int]):
    df = pd.read_csv(path, usecols=columns, header=None)
    return map(lambda i: df[i].to_numpy(), columns)
