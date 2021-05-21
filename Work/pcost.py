# pcost.py
#
# Exercise 1.27 - Michael King

# Calculate how much it costs to purchase all of the shares in the portfolio

total_cost = 0.0

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    #print(row)
    total_cost = int(row[1]) * float(row[2]) + total_cost

f.close()
print('Total cost', total_cost)
