import logging
import sys

# Set the logging level to DEBUG to catch any potential issues
logging.basicConfig(level=logging.DEBUG)

def calculate_something(a, b):
    """Calculate something based on a and b.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of the calculation.

    Raises:
        ValueError: If a is zero."
    if a == 0:
        raise ValueError("a cannot be zero")

    # Check for very large numbers and raise a ValueError if necessary
    if a > 1e10 or b > 1e10:
        raise ValueError("a or b is too large")

    result = a + b
    logging.debug(f"Result: {result}")
    return result

# Example usage
try:
    result = calculate_something(5, 10)
    print(result)
except ValueError as e:
    logging.error(f"Error: {e}")