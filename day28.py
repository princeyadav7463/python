# day 28
# set method in python

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))  # union is used to combine two sets and it returns a new set and it does not modify the original set
s1.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2) 
print(cities3)
print(cities.isdisjoint(cities2))  # isdisjoint is used to check if two sets are disjoint or not and it returns true or false value
print(cities.issubset(cities3))  # issubset is used to check if a set is subset of another set or not and it returns true or false value
print(cities3.issubset(cities)) 
cities.remove("Tokyo")  # remove is used to remove an element from the set
cities.discard("Tokyo2")  # discard is used to remove an element from the set and it does not raise an error if the element is not present in the set
item = cities.pop()  # pop is used to remove an element from the set and it returns the removed element and it removes the last element from the set

print(cities)
print(item)