def calculate_double_value(input_value):
    try:
        if not isinstance(input_value, (int, float)):
            raise TypeError("Input value must be a number")
        result = input_value * 2
        return result
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")
