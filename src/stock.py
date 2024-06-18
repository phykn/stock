import FinanceDataReader as fdr


def load_data(
    symbol,
    start = None,
    end = None,
    exchange = None,
    data_source = None,
):
    return fdr.DataReader(
        symbol = symbol,
        start = start,
        end = end,
        exchange = exchange,
        data_source = data_source
    )


def to_ror(prices):
    """convert from stock price to return of rate"""
    ror = prices[1:] / prices[:-1]
    ror = 100 * (ror - 1)
    return ror