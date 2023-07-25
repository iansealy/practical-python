# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        total = 0.0
        headers = next(rows)
        for name, shares, price in rows:
            try:
                total += int(shares) * float(price)
            except ValueError:
                print(f"Couldn't parse shares ({shares}) and/or price ({price})")
    return total

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
