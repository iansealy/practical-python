# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    if month == extra_payment_start_month:
        payment += extra_payment
    if month == extra_payment_end_month + 1:
        payment -= extra_payment
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if principal < 0:
        total_paid += principal
        principal = 0

    print(f"{month:3} {total_paid:9.2f} {principal:9.2f}")

print(f"Total paid {total_paid:0.2f}")
print(f"Months {month}")
