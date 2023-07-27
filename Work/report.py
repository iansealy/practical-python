# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            holding = dict(zip(headers, row))
            try:
                holding['shares'] = int(holding['shares'])
                holding['price'] = float(holding['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        change = prices[s['name']] - s['price']
        report.append((s['name'], s['shares'], prices[s['name']], change))
    return report

if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = 'Data/portfolio.csv'
    prices_filename = 'Data/prices.csv'

portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(' '.join([f'{h:>10s}' for h in headers]))
print(' '.join(['-' * 10 for _ in range(4)]))
for name, shares, price, change in report:
        price = f'${price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}')

bought = 0.0
current = 0.0
for s in portfolio:
        bought += s['shares']*s['price']
        current += s['shares']*prices[s['name']]
gain = current - bought
print(f"Current value: {current:0.2f}")
print(f"Gain/loss: {gain:0.2f}")
