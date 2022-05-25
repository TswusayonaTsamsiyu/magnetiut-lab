from pathlib import Path

from mgnt.common.fs import MAGNETISM_DIR, is_csv

PERMEABILITY_DIR = MAGNETISM_DIR / "1. Permeability"
AREA_TABLE = PERMEABILITY_DIR / "sizes.csv"


def get_material_path(material: str) -> Path:
    return PERMEABILITY_DIR / material.upper()


def get_measurement_path(material: str, resistance: int) -> Path:
    return get_material_path(material) / f"{resistance}k.csv"


def iter_material(material: str):
    return filter(is_csv, get_material_path(material).iterdir())
