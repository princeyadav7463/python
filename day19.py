# day 19
# list method in python 


l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)  # append is used to add a single element at the end of the list

# l.sort(reverse=True)  # sort is used to sort the list in ascending order
l.reverse()
print(l.index(1))  # index is used to find the index of the first occurrence of the element 
print(l.count(1))  # count is used to count the number of occurrences of the element
m = l.copy()  # copy is used to copy the list
m[0] = 0
l.insert(1, 899)  # insert is used to insert an element at a specific position
m[1] = 987
m = [900, 1000, 1100]  # m is a new list and it is not a copy of l
# l.extend(m)  # extend is used to add multiple elements at the end of the list

k=l+m  # concatenation of two lists
print(k)
print(l)