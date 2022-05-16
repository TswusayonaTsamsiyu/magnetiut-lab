from pathlib import Path
from socket import gethostname

GABI_LAPTOP = "LAPTOP-FFTKFOU5"
GABI_LAB_DIR = Path("H:/") / "My Drive" / "Labs"
ILAY_LAB_DIR = Path("G:/") / ".shortcut-targets-by-id" / "1qgY2gJharU3uwILQitDrQ7FqFqe7hwU0"
LAB_DIR = GABI_LAB_DIR if gethostname() == GABI_LAPTOP else ILAY_LAB_DIR
MAGNETISM_DIR = LAB_DIR / "Physics Lab B" / "4. Magnetism"
PERMEABILITY_DIR = MAGNETISM_DIR / "1. Permeability"
AREA_TABLE = PERMEABILITY_DIR / "sizes.csv"


def is_csv(path: Path) -> bool:
    return path.suffix == ".csv"


def get_material_path(material: str) -> Path:
    return PERMEABILITY_DIR / material.upper()


def get_measurement_path(material: str, resistance: int) -> Path:
    return get_material_path(material) / f"{resistance}k.csv"


def iter_material(material: str):
    return filter(is_csv, get_material_path(material).iterdir())
