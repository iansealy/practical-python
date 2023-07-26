# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = { "name" : row[0], "shares" : int(row[1]), "price" : float(row[2]) }
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

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
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
