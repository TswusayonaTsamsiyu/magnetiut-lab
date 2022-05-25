import pandas as pd

from mgnt.common.utils import cached

from .fs import AREA_TABLE
from .types import Measurement, Path

COLUMNS = [3, 4, 10]


def read_columns(path: Path, columns: list[int]):
    df = pd.read_csv(path, usecols=columns, header=None)
    return map(lambda i: df[i].to_numpy(), columns)


def parse_measurement(path: Path) -> Measurement:
    return Measurement(*read_columns(path, COLUMNS))


@cached
def parse_areas() -> dict:
    return dict(zip(*read_columns(AREA_TABLE, [0, 3])))


def to_csv(measurement):
    return "\n".join(map(lambda t: f"{t[0]}, {t[1]}", zip(measurement.Vr, measurement.Vc)))
