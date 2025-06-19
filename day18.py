# day 18
# list in python and list method in python 

marks = [3, 5, 1, 6, 9, "prince" , True, 6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[5])
print(len(marks))
print(marks[-3]) # negative index
print(marks[len(marks)-3]) # positive index
print(marks[8-3]) #positive index
print(marks[5]) # positive index


marks = [3, 5, 1, 6, 9, "prince" , True, 6]
if "prince" in marks:
    print("Yes")
else: 
    print("No")  

print(marks)  # list is mutable
print(marks[1:-1]) # slicing
print(marks[1:8]) # slicing
print(marks[1:8:2])  # slicing with step size
print(marks[1:8:3])  # slicing with step size and it will skip 2 elements and print the next element and so on 

lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(4) if i%2==0]
print(lst)

