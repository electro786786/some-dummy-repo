import os

# Follow PEP 8 naming convention
def calculate_something(input_value):
    try:
        # Restore the original calculation logic
        result = input_value * 2
        return result
    except Exception as e:
        # Handle potential exceptions
        print(f"An error occurred: {e}")
        return None