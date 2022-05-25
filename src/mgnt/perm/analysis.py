import pandas as pd

from mgnt.common.fitting import fit_linear
from mgnt.common.plotting import plot, plot_fit
from mgnt.common.utils import unzip, get_extrema

from .fs import get_measurement_path, iter_material
from .parsing import parse_measurement, parse_areas
from .types import Measurement, Axes, Path, Mat, Res

AIR_PERM_THEORY = 1.25663753e-6
AIR_PERM_MEASURED = 0.00312922
PROP = AIR_PERM_MEASURED / AIR_PERM_THEORY


def finde_die_spitze(measurement: Measurement) -> tuple:
    max_x, max_i, min_x, min_i = get_extrema(measurement.Vr)
    return max_x, measurement.Vc[max_i], min_x, measurement.Vc[min_i]


def plot_loop(axes: Axes, measurement: Measurement):
    axes.scatter(measurement.Vr, measurement.Vc)


def finde_die_spitzen(material: Mat):
    data = list(reversed(list(map(finde_die_spitze, map(parse_measurement, iter_material(material))))))
    return tuple(unzip(data))


def method_1(material: Mat) -> float:
    x, y = finde_die_spitzen(material)
    return fit_linear(x[:4], y[:4])[0] / PROP


def get_resistances(material: Mat) -> set:
    return set(map(lambda name: int(name[:-1]), map(lambda p: p.stem, iter_material(material))))


def get_area(material: Mat):
    return parse_areas()[material.upper()]


def method_2(mat1: Mat, mat2: Mat) -> float:
    res = max(get_resistances(mat1).intersection(get_resistances(mat2)))
    m1 = parse_measurement(get_measurement_path(mat1, res))
    m2 = parse_measurement(get_measurement_path(mat2, res))
    a, i, _, __ = get_extrema(m1.Vr)
    b, j, _, __ = get_extrema(m2.Vr)
    flux = m1.Vc[i] / m2.Vc[j]
    # chosen_max = min(a, b)
    # flux = m1.Vc[get_index(m1.Vr, chosen_max)] / m2.Vc[get_index(m2.Vr, chosen_max)]
    # areas = parse_areas()
    area = get_area(mat2) / get_area(mat1)
    return flux * area * b / a


def method_3(material: Mat, resistance: Res) -> float:
    m = parse_measurement(get_measurement_path(material, resistance))
    max_x, max_y, min_x, min_y = finde_die_spitze(m)
    return (max_y - min_y) / (max_x - min_x) / PROP


def plot_spitzen(material: Mat):
    with plot() as plt:
        x, y = finde_die_spitzen(material)
        plt.scatter(x, y)
        plot_fit(plt, lambda x_, a, b: a * x_ + b, x, fit_linear(x, y))
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")


def plot_loops(material: Mat):
    with plot() as plt:
        for measurement in map(parse_measurement, iter_material(material)):
            plot_loop(plt, measurement)
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")


def spitzen_to_csv(material: Mat, path: Path):
    data = list(reversed(list(map(finde_die_spitze, map(parse_measurement, iter_material(material))))))
    pd.DataFrame(data).to_csv(path, index=False, header=False)
