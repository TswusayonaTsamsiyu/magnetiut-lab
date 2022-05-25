from mgnt.common.fs import MAGNETISM_DIR

DOMAINS_DIR = MAGNETISM_DIR / "2. Domains"
IV_TABLE = DOMAINS_DIR / "VI.xlsx"


def is_bmp(path):
    return path.suffix == ".bmp"


def iter_images():
    return filter(is_bmp, DOMAINS_DIR.iterdir())


def get_image_path(arm, voltage):
    return DOMAINS_DIR / f"{arm}{voltage}.bmp"


def parse_voltage(path):
    return float(path.stem[1:])
