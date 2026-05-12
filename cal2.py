import math

def calculate_ratio(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers')
    if math.isnan(a) or math.isnan(b):
        raise ValueError('Inputs cannot be NaN')
    return math.sqrt(a) / math.sqrt(b)

# Example usage
print(calculate_ratio(4, 9))
