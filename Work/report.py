# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):
    return parse_csv(
        filename, select=["name", "shares", "price"], types=[str, int, float]
    )


def read_prices(filename):
    return dict(parse_csv(filename, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        change = prices[s["name"]] - s["price"]
        report.append((s["name"], s["shares"], prices[s["name"]], change))
    return report


def print_report(report):
    headers = ("Name", "Shares", "Price", "Change")
    print(" ".join([f"{h:>10s}" for h in headers]))
    print(" ".join(["-" * 10 for _ in range(4)]))
    for name, shares, price, change in report:
        price = f"${price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfolio.csv", "Data/prices.csv")
