from scipy.optimize import curve_fit


def fit_linear(x, y):
    return curve_fit(lambda x_, m, n: m * x_ + n, x, y)[0]
