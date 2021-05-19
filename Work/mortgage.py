# mortgage.py
#
# Exercise 1.8 - Michael King

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
extra_payment_duration = 12
months = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months +1

    if months >= 0 and months <= 12:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

print('Total paid', total_paid)
print('Months', months)
