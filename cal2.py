import math

def calculate(a, b):
    # Check for zero to avoid ValueError
    if a == 0:
        raise ValueError('Cannot divide by zero')

    # Check for NaN
    if math.isnan(a) or math.isnan(b):
        return None

    # Use a simple square root calculation for performance
    result = math.sqrt(a) + b

    return result

# Input validation to prevent security vulnerability
def validate_input(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Invalid input type')

# Example usage
validate_input(4, 5)
calculate(4, 5)
