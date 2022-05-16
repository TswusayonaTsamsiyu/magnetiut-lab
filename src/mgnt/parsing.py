import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from functools import lru_cache

from .fs import AREA_TABLE

COLUMNS = [3, 4, 10]


@dataclass
class Measurement:
    time: np.ndarray
    Vr: np.ndarray  # x
    Vc: np.ndarray  # y


def read_columns(path: Path, columns: list[int]):
    df = pd.read_csv(path, usecols=columns, header=None)
    return map(lambda i: df[i].to_numpy(), columns)


def parse_measurement(path: Path) -> Measurement:
    return Measurement(*read_columns(path, COLUMNS))


@lru_cache(None)
def parse_areas() -> dict:
    return dict(zip(*read_columns(AREA_TABLE, [0, 3])))
