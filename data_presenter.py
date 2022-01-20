# Problem 2
data = open('../CupcakeInvoices.csv')

# Problem 3
for row in data:
  print(row)

# Problem 4
for row in data:
  values = row.split(',')
  print(values[2])

  # Problem 5
for row in data:
  values = row.split(',')
  total = int(values[3]) * float(values[4])
  print(total)

# Problem 6
total = 0

for row in data:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(total)

# Problem 7
data.close()