import numpy as np
import matplotlib.pyplot as plt
from contextlib import contextmanager

from .parsing import Measurement

FIT_CURVE_DENSITY = 1000


def plot_loop(axes: plt.Axes, measurement: Measurement):
    axes.scatter(measurement.Vr, measurement.Vc)


def plot_fit(axes, fit, xdata, params, **kwargs):
    xdata = np.linspace(xdata[0] + xdata[0] * 0.1, xdata[-1] + xdata[-1] * 0.1, FIT_CURVE_DENSITY)
    return axes.plot(xdata, fit(xdata, *params), **kwargs)


@contextmanager
def plot():
    fig, axes = plt.subplots()
    try:
        yield axes
    finally:
        fig.show()
