import pandas as pd
from pathlib import Path

from .fitting import fit_linear
from .plotting import plot, plot_loop, plot_fit
from .fs import get_measurement_path, iter_material
from .parsing import parse_measurement, parse_areas
from .utils import finde_die_spitze, unzip, get_max, get_index

PROP = 0.00312922


def finde_die_spitzen(material: str):
    data = list(reversed(list(map(finde_die_spitze, map(parse_measurement, iter_material(material))))))
    return tuple(unzip(data))


def method_1(material: str) -> float:
    x, y = finde_die_spitzen(material)
    return fit_linear(x[:4], y[:4])[0] / PROP


def get_resistances(material: str) -> set:
    return set(map(lambda name: int(name[:-1]), map(lambda p: p.stem, iter_material(material))))


def get_area(material: str):
    return parse_areas()[material.upper()]


def method_2(mat1: str, mat2: str) -> float:
    res = max(get_resistances(mat1).intersection(get_resistances(mat2)))
    m1 = parse_measurement(get_measurement_path(mat1, res))
    m2 = parse_measurement(get_measurement_path(mat2, res))
    a, i = get_max(m1.Vr)
    b, j = get_max(m2.Vr)
    flux = m1.Vc[i] / m2.Vc[j]
    # chosen_max = min(a, b)
    # flux = m1.Vc[get_index(m1.Vr, chosen_max)] / m2.Vc[get_index(m2.Vr, chosen_max)]
    areas = parse_areas()
    area = get_area(mat2) / get_area(mat1)
    return flux * area * b / a


def plot_spitzen(material: str):
    with plot() as plt:
        x, y = finde_die_spitzen(material)
        plt.scatter(x, y)
        plot_fit(plt, lambda x_, a, b: a * x_ + b, x, fit_linear(x, y))
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")


def plot_loops(material: str):
    with plot() as plt:
        for measurement in map(parse_measurement, iter_material(material)):
            plot_loop(plt, measurement)
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")


def spitzen_to_csv(material: str, path: Path):
    data = list(reversed(list(map(finde_die_spitze, map(parse_measurement, iter_material(material))))))
    pd.DataFrame(data).to_csv(path, index=False, header=False)
