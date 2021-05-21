# pcost.py
#
# Exercise 1.30 - Michael King

# Turning script from exercise 1.27 into a function

def portfolio_cost(filename):

    total_cost = 0.0

    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        row = line.split(',')
        #print(row)
        total_cost = int(row[1]) * float(row[2]) + total_cost

    return total_cost

#f.close()
cost = portfolio_cost(filename)
print('Total cost', cost)
