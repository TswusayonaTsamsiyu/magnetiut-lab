from .fitting import fit_linear
from .parsing import parse_measurement
from .utils import finde_die_spitze, unzip
from .plotting import plot, plot_loop, plot_fit
from .fs import get_measurement_path, iter_material


def plot_spitzen(material: str) -> tuple:
    with plot() as plt:
        data = list(reversed(list(map(finde_die_spitze, map(parse_measurement, iter_material(material))))))
        x, y = tuple(unzip(data))
        m, n = fit_linear(x, y)
        plt.scatter(x, y)
        plot_fit(plt, lambda x_, a, b: a * x_ + b, x, (m, n))
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")
        return m, n


def plot_loops(material: str):
    with plot() as plt:
        for measurement in map(parse_measurement, iter_material(material)):
            plot_loop(plt, measurement)
        plt.set(xlabel="Vr [V]", ylabel="Vc [V]")
