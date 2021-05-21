# pcost.py
#
# Exercise 1.33 - Michael King

# Reading from the command line

import sys
import csv

def portfolio_cost(filename):

    total_cost = 0.0

    f = open(filename)
    rows = csv.reader(f)
    headers = next(f)
    for line in f:
        try:
            row = line.split(',')
            #print(row)
            total_cost = int(row[1]) * float(row[2]) + total_cost
        except ValueError:
            print('Bad row', row)

    return total_cost

if len(sys.argv) ==2:
    filename = sys.argv[1]
else:
 filename = 'Data/portfolio.csv'

#f.close()
cost = portfolio_cost(filename)
print('Total cost:', cost)
