import numpy as np
import numba as nb
from .cauchy import cauchy


@nb.njit
def numba_choice(population, weights, k):
    wc = np.cumsum(weights)
    m = wc[-1]
    sample = np.empty(k, population.dtype)
    sample_idx = np.full(k, -1, np.int32)

    i = 0
    while i < k:
        r = m * np.random.rand()
        idx = np.searchsorted(wc, r, side='right')
        for j in range(i):
            if sample_idx[j] == idx:
                continue

        sample[i] = population[idx]
        sample_idx[i] = population[idx]
        i += 1

    return sample


def generate(
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
    rs = numba_choice(z, weights = p, k = num)
    for r in rs:
        x.append((1 + r / 100) * x[-1])
    
    return np.array(x)