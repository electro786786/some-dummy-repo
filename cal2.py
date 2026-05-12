import math

def calculate_square_root_ratio(num1, num2):
    if num2 == 0:
        raise ValueError('Denominator cannot be zero')
    square_root_ratio = math.sqrt(num1) / math.sqrt(num2)
    return square_root_ratio

# Example usage
result = calculate_square_root_ratio(9, 4)
print(result)
