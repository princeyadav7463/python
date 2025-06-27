# day 33
# finally keyword in python  

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 0
  except:
    print("Some error occurred")
  finally:  # finally is used to execute the code regardless of the error
    print("I am always executed") 
    # print("I am always executed")


x= func1()
print(x)
