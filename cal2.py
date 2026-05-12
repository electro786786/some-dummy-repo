import math

def calculate_ratio(a, b):
    if a == 0:
        raise ValueError('a cannot be zero')
    if b == 0:
        raise ValueError('b cannot be zero')
    sqrt_a = math.sqrt(a)
    ratio = sqrt_a / math.sqrt(b)
    return ratio

# Example usage:
print(calculate_ratio(4, 9))
