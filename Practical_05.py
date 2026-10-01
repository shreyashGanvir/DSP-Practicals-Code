# Program 1: Built-in Module (math)
import math

num = 16

print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))

# Program 2: Functional Programming Module
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", result)

# Program 3: User-defined Module
import my_module

print("Addition:", my_module.add(5, 3))
print("Multiplication:", my_module.multiply(4, 2))
