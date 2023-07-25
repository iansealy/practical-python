# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    total = 0.0
    headers = next(f).strip().split(',')
    for line in f:
        (name, shares, price) = line.strip().split(',')
        total += int(shares) * float(price)
print(f'Total cost {total:0.2f}')
