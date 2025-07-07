# day 40

for x in range(1, 11):
 if x%2==1:
  print(x)

for x in range(1, 11):
  if x%2==1:
    print(x)

for x in range(1, 11):
  if x%3==0 and x%5==0:
    print(x)



# factorial of a number
fact=1
for x in range(1, 6):
  fact=fact*x
print(fact)


# sumation of series
sum = 0                     # sum of two number = x*x  sum of queue = x*x*x
for x in range(1, 11):
  sum=sum+x
print(sum)

sum = 0
for x in range(1, 11):
 if x%2==0:
   sum = sum+x
print(sum)

sum = 0
for x in range(1, 11):
  if x%2==1:
    sum = sum+x**x
print(sum)


sum =0
for x in range(1,5):
  sum = sum+x**(x+1)
print(sum)


# 1+2-3+4-5+6-7+8-9+10
sum = 0
for x in range(1, 10):
  if x%2==0:
   sum = sum-x
else:
   sum = sum+x
print(Sum)

x = 0
while x <= 10:
  if x%2 ==0:
    print(x)
  x=x+1


x = 3
if x > 0:
  print("true")
if x < 0:
  print("false")
if x!=0:
  print("true")
