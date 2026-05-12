import logging

logging.basicConfig(level=logging.INFO)

def calculate_something(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both a and b must be numbers')
    if b == 0:
        raise ValueError('Cannot divide by zero')
    result = a / b
    return result

# Example usage
result = calculate_something(10, 2)
print(result)
