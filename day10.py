# day 10
#  if else statement
a = int(input("Enter your age: "))
print("Your age is:", a) 
 # conditional operators
 # >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
print("Yay!")  # this will be printed regardless of the condition

# /if-elif-else ladder in python

num = int(input("Enter the value of num: "))
if(num<0):
  print("Number is negative.")
elif(num == 0):
  print("Number is Zero.")
elif(num == 999):
  print("Number is special.")
else:
  print("Number is positive.") 

print("I am happy now")  

# nested if else statement
num = 18
if(num<0):
  print("Number is negative.")
elif(num>0): 
  if(num<=10): # nested if else statement
    print("Number is between 1-10")
  elif(num>10 and num<=20): # and is used to check if both the conditions are true or not and it returns true or false value
    print("Number is between 11-20")
  else:
    print("Number is greater than 20")
else:
 print("Number is Zero") 
