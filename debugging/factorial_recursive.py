#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given integer using recursion.

def factorial(n):
    # Parameters:
    # n: an integer for which the factorial is to be calculated.
    
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: multiply n with the factorial of (n-1)
        return n * factorial(n-1)

# Calculate the factorial of the integer provided as a command-line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)

# Returns:
# The factorial of the provided integer.

