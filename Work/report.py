#report.py
#
# Exercise 3.15 - Michael King

import csv
import fileparse

#Read the portfolio using fileparse

def read_portfolio(filename):
    '''Opens a csv file and reads it into a list of dictionaries'''
    
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

##Read the prices into a dictionary using fileparse

def read_prices(filename):
    '''Reads prices into a dictionary'''
    
    return dict(fileparse.parse_csv(filename, types=[str,float], has_headers = False))

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

# Main function

def main(args):
    
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    main()




