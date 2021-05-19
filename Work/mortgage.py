# mortgage.py
#
# Exercise 1.11 - Michael King

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
extra_payment_duration = 12
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
last_month = 310
last_payment = 809.21

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months +1

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    elif months >= last_month:
        principal = principal - principal
        total_paid = total_paid + last_payment



    print(months, total_paid, principal)
print('Total paid', total_paid)
print('Months', months)
