# pcost.py
#
# Exercise 1.31 - Michael King

# Error Handling

def portfolio_cost(filename):

    total_cost = 0.0

    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        try:
            row = line.split(',')
            #print(row)
            total_cost = int(row[1]) * float(row[2]) + total_cost
        except ValueError:
            print('Bad row', row)

    return total_cost

#f.close()
cost = portfolio_cost(filename)
print('Total cost', cost)
