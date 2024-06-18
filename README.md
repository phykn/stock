# Simulated Stock Prices using Cauchy Distribution

This project simulates stock prices using a Cauchy distribution to model the rate of return. The simulation generates multiple stock price series and visualizes their behavior over time.

## Description

The main idea is to use a Cauchy distribution to generate random rates of return for stock prices. This distribution is chosen due to its heavy tails, which can model the extreme fluctuations often observed in stock prices.

## Installation

To run this project, you need Python 3.x and the following libraries:
- numpy
- numba
- matplotlib
- scikit-learn
- scipy
- finance-datareader

You can install the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Example
```python
from src.cauchy import generate_data

x = generate_data(
    init_value = 100,  # initial value
    x0 = 0.0,          # center of the rate of return
    gamma = 1.0,       # variance of the rate of return
    num = 1000,        # number of x points
    rmin = -10,        # minimum value of the rate of return
    rmax = 10,         # maximum value of the rate of return
    rnum = 1000        # number of r points
)

print(x)
>>> array([100.        , 101.53153153, 100.05785064, ..., 364.99559152,
           364.22833351, 360.40010779])
```