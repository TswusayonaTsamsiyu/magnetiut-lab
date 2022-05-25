import numpy as np

from mgnt.common.plotting import plot
from mgnt.common.fs import MAGNETISM_DIR, is_csv
from mgnt.perm.analysis import plot_loop, parse_measurement

CURIE_DIR = MAGNETISM_DIR / "3. Curie"
E = 5


def parse_temp(path):
    return float(path.stem)


def get_y_at_0(measurement):
    index = np.where(abs(measurement.Vr) < E)[0][0]
    return abs(measurement.Vc[index])


def plot_m2t():
    m = []
    t = []
    for path in sorted(filter(is_csv, CURIE_DIR.iterdir()), key=parse_temp):
        measurement = parse_measurement(path)
        m.append(get_y_at_0(measurement))
        t.append(parse_temp(path))
    with plot() as plt:
        plt.scatter(t, m)
        plt.set(xlabel="T", ylabel="~M")


def plot_loops():
    with plot() as plt:
        for path in sorted(filter(is_csv, CURIE_DIR.iterdir()), key=parse_temp):
            measurement = parse_measurement(path)
            plot_loop(plt, measurement, label=str(parse_temp(path)))
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")
        plt.legend()
