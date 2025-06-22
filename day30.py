# day 30
# dictionary method in python

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)  # update is used to update the dictionary with the elements from another dictionary
print(ep1)

ep1. pop(122)  # pop is used to remove the key-value pair from the dictionary
print(ep1)

ep1.popitem()  # popitem is used to remove the last key-value pair from the dictionary
del ep1[123]  # del is used to delete the key-value pair from the dictionary
print(ep1)
