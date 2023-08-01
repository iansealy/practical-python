# pcost.py
#
# Exercise 1.27

import csv
import sys

import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    total_cost = 0.0
    for record in portfolio:
        total_cost += record["shares"] * record["price"]
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
