# report.py
#
# Exercise 3.2 - Michael King

import csv

def read_portfolio(filename):
    '''Opens a csv file and reads it into a list of dictionaries'''
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


def make_report_data(portfolio,prices):
    """Create data that will go into a report"""
    rows = []
    for s in portfolio:
        current_price = prices[s['name']] ##Current share price
        change = current_price - s['price'] ##Change in the share price
        summary = (s['name'], s['shares'], current_price, change) ##List of tuples
        rows.append(summary)
    return rows

##Exercise 3.1 Make a print report function

def print_report(reportdata):

    """Prints the report"""

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

#Exercise 3.2 Creating a top level function for porgram execution

def portfolio_report(portfile,pricefile):

    """Make a report based on stock data taken from files"""

    portfolio = read_portfolio(portfile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolio, prices)

    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
