import math

def calculate_something(a, b):
    if a == 0:
        raise ValueError('a cannot be zero')
    if b == 0:
        raise ValueError('b cannot be zero')
    try:
        result = math.sqrt(a) / math.sqrt(b)
        return result
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

# Example usage
print(calculate_something(4, 9))
