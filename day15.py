# day 15
# break and continue statement in python

for i in range(12):
  if(i == 10):
   print("Skip the iteration")
   continue
    # break
  print("5 X", i+1, "=", 5 * (i+1))  # this will print 5 times table till 10

while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
      break
      print(i)   # this will print 1 to 100 and then break the loop