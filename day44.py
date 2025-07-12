# day 44

# map filter and reduce in python
#  the map function in python is used to apply a function to all the items in an input list. The map function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
def cube(x):
  return x*x*x


print(cube(2))

l = [1, 2, 4, 6, 45, 4]
# newl = []
# for item in l
# newl = list(map(lambda x: x*x*x, l))

# newl = list(map(cube, l))
newl = list(map(lambda x: x*x*x, l))
print(newl)

# filter function in python
# filter function in python is used to filter the elements of an iterable (list, tuple etc.) based on a function. The filter function returns a list of elements for which the function returns true.

def filter_function(a):
  return a>4

newnewl = list(filter(filter_function, l))
print(newnewl)



from functools import reduce
numbers = [1, 2, 3, 4, 5]

def mysum(x, y):
  return x + y

sum = reduce(mysum, numbers)
#  print the sum  of the numbers in the list
print(sum)


# is or == in python 
# is or == in python is used to check if two variables are equal or not and it returns true or false value and it is used to check if two variables are pointing to the same object or not and it returns true or false value 

a = 3
b = 3
print(a is b)
print(a == b)

