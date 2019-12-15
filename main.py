#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "cdanjha"


def add(x, y):
    # """Add two integers. Handles negative values."""
     # your code here
    total = x + y
    return total
# when i first started this i misread the instructions and thought
# it read "without using + or -" so thats what i did research on


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if y < 0:
        return -multiply(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)

print(multiply(6, -8))



def power(x, n): 
    """Raise x to power n, where n >= 0"""
    # your code here
    if (n == 0): return 1
    elif (int(n % 2) == 0): 
        return (power(x, int(n / 2)) *
               power(x, int(n / 2))) 
    else: 
        return (x * power(x, int(n / 2)) *
                   power(x, int(n / 2))) 
  
x = 2; n = 8
print(power(x, n))


    
def factorial(x):
    """Compute factorial of x, where x > 0"""
    # your code here
    f = 1
    for num in range(2, x + 1):
        f *= num
    return f
print(factorial(4))


def fibonacci(n): 
    """Compute the nth term of fibonacci sequence"""
    # your code here
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)
print fibonacci(8)



if __name__ == '__main__':
    # your code to call functions above
    pass
