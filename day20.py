# day 22
# tuple in python
# A tuple is an ordered collection of items (elements) that is immutable (cannot be changed after creation). Tuples are defined using parentheses () and elements are separated by commas.

# Key Characteristics of Tuples:
# Ordered - Items have a defined order that won't change
# Immutable - You cannot change, add, or remove items after creation
# Allow duplicates - Can contain the same value multiple times
# Indexed - Access items using index numbers (starting from 0)
# Let me add more comprehensive tuple examples to your code:
# tuple is immutable and it is faster than list and it is used to store the data which is not going to change.

tup = (1, 2, 76, 342, 32, "green", True)  
print(tup) 
print(type(tup) , tup) # type is used to find the type of the variable
print(tup[0]) # indexing
print(tup[1])
print(tup[2])
print(tup[3]) 

if 342 in tup: # in is used to check if the element is present in the tuple or not and it returns true or false value
    print("Yes 342 is present in this tuple")
else:
    print("No 342 is not present in this tuple")  
