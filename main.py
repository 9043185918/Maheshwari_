# python
def factorial (n):
   if n==0:
     return 1
   else:
     return n* factorial (n-1)
# Example usage:
numbers=5
result=factorial(numbers)
print(f"The factorial of{numbers} is{result}")