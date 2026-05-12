import logging

def calculate_something(a, b):
    """
    This function calculates something based on the input values a and b.

    Args:
        a (int): The first input value.
        b (int): The second input value.

    Returns:
        int: The calculated result.

    Raises:
        ValueError: If a or b is too large.
    """
    if a > 1000 or b > 1000:
        raise ValueError("Input values a and b cannot be larger than 1000")
    # Rest of the function remains the same
    result = a + b
    return result

# Example usage
try:
    result = calculate_something(500, 500)
    logging.error("Result: %s", result)
except ValueError as e:
    logging.error("Error: %s", e)
