# pcost.py
#
# Exercise 3.15 - Michael King

# main() functions

import sys
import csv
import report

def portfolio_cost(filename):

    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

def main(args):

    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    main()
