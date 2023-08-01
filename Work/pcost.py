# pcost.py
#
# Exercise 1.27

import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    total_cost = 0.0
    for record in portfolio:
        total_cost += record["shares"] * record["price"]
    return total_cost


def main(argv):
    if len(argv) == 2:
        cost = portfolio_cost(argv[1])
    else:
        cost = portfolio_cost("Data/portfolio.csv")
    print("Total cost:", cost)


if __name__ == "__main__":
    import sys

    main(sys.argv)
