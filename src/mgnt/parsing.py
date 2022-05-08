import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass

from .utils import get_max

COLUMNS = [3, 4, 10]


@dataclass
class Measurement:
    time: np.ndarray
    Vr: np.ndarray  # x
    Vc: np.ndarray  # y


def parse_measurement(path: Path) -> Measurement:
    df = pd.read_csv(path, usecols=COLUMNS, header=None)
    return Measurement(*map(lambda i: df[i].to_numpy(), COLUMNS))
