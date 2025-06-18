# day 13
# loop in python

name = 'Prince'
for i in name:
    print(i, end=", ")
    if(i == "n"):
        print("This is something special!")  # this will be printed when i is equal to n 

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)    # this will print each character of the color

for k in range(5):
  print(k+1)  # this will print 1 to 5

for k in range(1, 20):
  print(k)  # this will print 1 to 19

for k in range(1, 12, 3):  # 3 is the step size
  print(k)