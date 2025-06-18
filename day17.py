# day 17
# function arguments in python

def average(a=9, b=1):
   print("The average is ", (a+b)/2)  # default argument

average(4, 6) 
average(b=8, a=21)

def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("The average is ", sum / len(numbers))
  return sum / len(numbers)
c = average(5, 6, 7, 1)
print(c)

def name(**name):
  print("Hello,", name["fname"], name["mname"], name["lname"])  

name(mname = "Buchanan", lname = "Barnes", fname = "James")