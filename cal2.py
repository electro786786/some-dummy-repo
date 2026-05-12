def calculate_distance(a, b):
    """
    Calculate the Euclidean distance between two points.

    Args:
        a (float): The x-coordinate of the first point.
        b (float): The y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.

    Raises:
        ValueError: If a is zero
    """
    if a == 0:
        raise ValueError("Cannot calculate distance when a is zero")

    distance_squared = a ** 2 + b ** 2
    distance = distance_squared ** 0.5
    return distance

# Example usage:
print(calculate_distance(3, 4))