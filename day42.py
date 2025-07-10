# day 42
# local or gobal variable in python
x = 4  # global variable 
# global variable is a variable that is defined outside of a function and it is accessible from anywhere in the program and it is not dependent on the function 
print(x)


def hello():
  x=5  # local variable local variable is a variable that is defined inside of a function and it is only accessible from within that function and it is dependent on the function
  y=1
  print(f"The local x is {x}")
  print(f"The local y is {y}")

print(f"The global x is {x}")
hello()
x = 88
print(f"The global x is {x}")