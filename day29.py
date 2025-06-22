# day 29
# dictionary in python

dic = {
  344: "Prince",
  56: "John",
  567: "Rahul",
  566: "zakir",
  123: "Rohan"
}
print(dic[344])  # indexing is used to access the value of the key

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
# print(info['name2'])  # this will throw an error as name2 is not present in the dictionary
print(info.get('name2'))  # this will not throw an error as name2 is not present in the dictionary and it will return none
print(info.keys())  # keys is used to get all the keys of the dictionary 

print(info.items())  # items is used to get all the items of the dictionary and it returns a list of tuples
for key , value in info.items():
  print(f"The value corresponding to the key {key} is {value}")
