# day 26
# Recursion in python


# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(7))
print(factorial(5))
print(factorial(4))
print(factorial(3))



def fibonacci_recursive(n):
  if n <= 1:
      return n
  else:
      return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
num = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(num):
  print(fibonacci_recursive(i), end=" ")