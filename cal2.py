import math

def calculate_distance(a, b):
    """
    Calculate the distance between two points.

    Args:
        a (float): The x-coordinate of the first point.
        b (float): The y-coordinate of the second point.

    Returns:
        float: The distance between the two points.

    Raises:
        ValueError: If a is zero
    """
    if a == 0:
        raise ValueError("a cannot be zero")

    # Calculate the square root of the product of a and b
    sqrt_product = math.sqrt(a * b)

    # Calculate the distance
    distance = sqrt_product

    return distance

# Example usage
a = 4
b = 16
distance = calculate_distance(a, b)
print(distance)
