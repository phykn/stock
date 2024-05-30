import random
import numpy as np


def cauchy(x, a, x0, gamma):
    """
    x: rate of return
    a: constant
    x0: center of the rate of return
    gamma: variance of the rate of return
    """
    return a * gamma / (np.power(x - x0, 2) + np.power(gamma, 2))


def generate_data(
        init_value = 100, 
        x0 = 0.0, 
        gamma = 1.0, 
        num = 1000, 
        rmin = -10, 
        rmax = 10, 
        rnum = 1000
    ):
    """
    init_value: initial value
    x0: center of the rate of return
    gamma: variance of the rate of return
    num: number of x points
    rmin: minimum value of the rate of return
    rmax: maximum value of the rate of return
    rnum: number of r points
    """
    z = np.linspace(rmin, rmax, num = rnum)
    p = cauchy(z, a = 1, x0 = x0, gamma = gamma)
    p = p / np.sum(p)

    x = [init_value]
    rs = random.choices(z, weights = p, k = num)
    for r in rs:
        x.append((1 + r / 100) * x[-1])
    
    return np.array(x)