# report.py
#
# Exercise 2.16 - Michael King

import csv

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of dictionary'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))  ## Added for Exercise 2.16
            dict_stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(dict_stock)

    return portfolio

##Exercise 2.6 - Read the prices into a dictionary

def read_prices(filename):
    '''Reads prices into a dictionary'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

##Exercise 2.7 - Finding out if you can retire
#Read both dictionaries 
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Total cost of the portfolio from portfolio.csv
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Current value of the portfolio from prices.csv
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)

##Exercise 2.9 - Collecting Data

def make_report(portfolio,dict):
    """Makes a report"""
    rows = []
    for s in portfolio:
        current_price = prices[s['name']] ##Current share price
        change = current_price - s['price'] ##Change in the share price
        summary = (s['name'], s['shares'], current_price, change) ##List of tuples
        rows.append(summary)
    return rows

##Exercise 2.11 - Adding some headers

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
