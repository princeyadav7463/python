# day 34
# raise keyword in python
# The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
a = int(input("Enter any value between 5 and 9: "))

if(a<5 or a>9):
  raise ValueError("Value should be between 5 and 9")  # raise is used to raise an exception and it is used to throw an error 
