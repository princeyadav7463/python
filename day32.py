# day 32
# exception handling in python

'''Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handiling deals with these events to avoid the program or system crashing, and without this process, exception would disrupt the normal operation of a program.

Exception in Python 
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.'''


a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:  # Exception as e:  # this will print the error message
  print("Invalid input!")
for i in range(1, 11):
  # print(f"{int(a)} X {i} = {int(a)*i}")
  print(f"{int(a)} X {i} = {int(a)*i}")  # this will throw an error if the input is not a number 

print("Some imp lines of code")  # this will not be printed as the program will crash
print("End of program")

try:
  num = int(input("Enter an integer: "))
  a=[6, 3]
  print(a[num])
except ValueError:
  print("Number entered is not an integer.")
except IndexError:
  print("Index Error")
