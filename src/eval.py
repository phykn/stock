import numpy as np
import matplotlib.pyplot as plt
from .stock import load_data, to_ror
from .fit import cauchy_fit


def daily_to_annual(rate_of_return):
    return 100 * (1 + rate_of_return / 100) ** 250 - 100


def eval(symbol, start = '1980', plot = False):
    df = load_data(symbol = symbol, start = start)
    df = df.dropna()

    prices = df['Close'].values
    ror = to_ror(prices)
    out = cauchy_fit(ror, return_xyz = True)

    if plot:
        plt.figure(figsize = (12, 4))

        plt.subplot(1, 3, 1)
        plt.title(symbol)
        df['Close'].plot(color = 'k')
        plt.ylim(bottom = 0)
        plt.ylabel('Price ($)')

        plt.subplot(1, 3, 2)
        np.log10(df['Close']).plot(color = 'k')
        plt.ylabel('Log Price')

        plt.subplot(1, 3, 3)
        plt.title(f"(x0, gamma) = ({out['x0']:.2f}, {out['gamma']:.2f})")
        plt.scatter(out['x'], out['y'], color = 'orange', s = 5)
        plt.plot(out['x'], out['z'], color = 'r')
        plt.xlim(out['x'].min(), out['x'].max())
        plt.ylim(0, 1.5 * out['z'].max())
        plt.xlabel('rate of return (%)')
        plt.ylabel('Density')

        plt.tight_layout()
        plt.show()

    rate_of_return = out['x0']
    risk = out['gamma']

    return rate_of_return, risk