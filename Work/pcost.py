# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        total = 0.0
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            name, shares, price = row
            try:
                total += int(shares) * float(price)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
