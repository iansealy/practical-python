# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total = 0.0
        headers = next(f).strip().split(',')
        for line in f:
            (name, shares, price) = line.strip().split(',')
            try:
                total += int(shares) * float(price)
            except ValueError:
                print(f"Couldn't parse shares ({shares}) and/or price ({price})")
    return total

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
