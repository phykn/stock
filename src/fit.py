import numpy as np
from sklearn.neighbors import KernelDensity
from scipy.optimize import curve_fit
from .cauchy import cauchy


def cauchy_fit(arr, n_pt = 1000, return_xyz = False):
    std = np.std(arr)
    kde = KernelDensity(
        kernel = 'epanechnikov', 
        bandwidth = 0.01 * std
    ).fit(arr[:, None])

    x = np.linspace(-5 * std, 5 * std, num = n_pt)
    y = np.exp(kde.score_samples(x[:, None]))
    opt, _ = curve_fit(cauchy, x, y)

    a, x0, gamma = opt

    if return_xyz:
        return dict(
            a = a,
            x0 = x0,
            gamma = gamma,
            x = x,
            y = y,
            z = cauchy(x, a, x0, gamma)
        )
    else:
        return dict(
            a = a,
            x0 = x0,
            gamma = gamma
        )