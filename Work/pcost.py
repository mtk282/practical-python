# pcost.py
#
# Exercise 3.14 - Michael King

# Using more library imports

import sys
import csv
import report

def portfolio_cost(filename):

    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

if len(sys.argv) ==2:
    filename = sys.argv[1]
else:
 filename = 'Data/portfoliodate.csv'

#f.close()
cost = portfolio_cost(filename)
print('Total cost:', cost)
