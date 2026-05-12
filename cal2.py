import math

def calculate_square_root_ratio(numerator, denominator):
    """
    Calculate the square root ratio of two numbers.

    Args:
        numerator (float): The numerator of the ratio.
        denominator (float): The denominator of the ratio.
    """
    ratio = math.sqrt(numerator / denominator)
    return ratio

# Example usage:
# ratio = calculate_square_root_ratio(9, 16)
