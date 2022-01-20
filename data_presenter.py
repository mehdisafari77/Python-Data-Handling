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

import matplotlib.pyplot as plt 
    
# x axis values 
x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"] 
# y axis values 
y = [10,40,32,84,60,52,18] 
    
# plotting  points  
plt.plot(x, y) 
    
# naming x axis 
plt.xlabel('Day Purchased') 
# naming y axis 
plt.ylabel('Cupcakes Purchased') 
    
# giving a title to graph 
plt.title('My Cupcake Sales') 
    
# function to show plot 
plt.show() 