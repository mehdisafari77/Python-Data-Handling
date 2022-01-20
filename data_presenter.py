# Problem 2
data = open('../CupcakeInvoices.csv')

# Problem 3
for row in data:
  print(row)

# Problem 4
for row in data:
  values = row.split(',')
  print(values[2])