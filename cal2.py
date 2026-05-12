import math

def calculate_ratio(a, b):
    """
    Calculate the ratio of the square root of a to the square root of b.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The ratio of the square root of a to the square root of b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)

    ratio = sqrt_a / sqrt_b

    return ratio

# Example usage:
print(calculate_ratio(4, 9))