#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) != 2:
    print("Usage: python3 script_name.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

if n < 0:
    print("Factorial is not defined for negative numbers.")
    sys.exit(1)

f = factorial(n)
print(f)

