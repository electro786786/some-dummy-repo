import sys

# Function to calculate something
def calculate_something(a, b):
    if b == 0:
        raise ValueError('b cannot be zero')
    if a > 1e10 or b > 1e10:
        raise ValueError('a or b is too large')
    # Rest of the function remains the same

# Example usage
try:
    calculate_something(10, 20)
except ValueError as e:
    print(e)
