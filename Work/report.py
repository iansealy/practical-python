# report.py

import fileparse
import tableformat
from portfolio import Portfolio


def read_portfolio(filename, **opts):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as file:
        portfolio = Portfolio.from_csv(file)

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) == 3:
        portfolio_report(args[1], args[2])
    elif len(args) == 4:
        portfolio_report(args[1], args[2], args[3])
    else:
        raise SystemExit("Usage: %s portfile pricefile format" % args[0])


if __name__ == "__main__":
    import logging
    import sys

    logging.basicConfig(
        filename="app.log",  # Name of the log file (omit to use stderr)
        filemode="w",  # File mode (use 'a' to append)
        level=logging.WARNING,  # Logging level (DEBUG, INFO, WARNING, ERROR, or
        # CRITICAL)
    )

    main(sys.argv)
