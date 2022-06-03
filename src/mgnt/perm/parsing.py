from mgnt.common.utils import cached, read_columns

from .fs import AREA_TABLE
from .types import Measurement, Path

COLUMNS = [3, 4, 10]


def parse_measurement(path: Path) -> Measurement:
    return Measurement(*read_columns(path, COLUMNS))


@cached
def parse_areas() -> dict:
    return dict(zip(*read_columns(AREA_TABLE, [0, 3])))


def to_csv(measurement):
    return "\n".join(map(lambda t: f"{t[0]}, {t[1]}", zip(measurement.Vr, measurement.Vc)))
