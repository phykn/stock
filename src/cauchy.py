import numpy as np


def cauchy(x, a, x0, gamma):
    """
    x: rate of return
    a: constant
    x0: center of the rate of return
    gamma: variance of the rate of return
    """
    return a * gamma / (np.power(x - x0, 2) + np.power(gamma, 2))