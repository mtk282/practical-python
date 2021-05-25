# report.py
#
# Exercise 2.5 - Michael King

import csv

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of dictionary'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            dict_stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(dict_stock)

    return portfolio
