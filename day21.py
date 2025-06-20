# day 21

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
contries = tuple(temp)
print(contries)
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)   # count is used to count the number of occurrences of the element
res = tuple1.index(3, 4, 8)  # index is used to find the index of the first occurrence of the element
print('Count of 3 in tuple1 is:', res)  # count is used to count the number of occurrences of the element
