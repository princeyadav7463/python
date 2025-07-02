# day 38
# How import works in python?
'''
 Importing in pythong is the process of loading code from a python module into the current script. This allows you to use the functions, and variables defined in the module in your current script, as well as any additinlal modules that the imported module may depend on.

 To import a module in Python you use the import statement follwed by the module. for example. to import the math module, which contains a variety of mathematical functions, you would use the following statement:
 # import math
 Once a module is imported, you can use any of the function and variables defined in the module by using the dot notation. for example, to use the sqrt function from the math module, you would write:
 '''
 # import math
 result = math.sqrt(16)
 print(result)  # Output: 4.0

 import pandas
 pansdas.read_csv("data.csv")

 def welcome():
   print("Hey you are welcome here")  