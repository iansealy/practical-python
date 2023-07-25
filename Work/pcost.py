# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total = 0.0
        headers = next(f).strip().split(',')
        for line in f:
            (name, shares, price) = line.strip().split(',')
            total += int(shares) * float(price)
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
