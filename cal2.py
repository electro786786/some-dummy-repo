import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def calculate_something(input_data):
    try:
        # Perform meaningful calculation
        result = input_data * 2
        return result
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        return None

def main():
    # Remove this function as it's not necessary
    pass

# Rename function1 and function2 to something more descriptive
def perform_calculation(input_data):
    return calculate_something(input_data)

# Example usage
if __name__ == '__main__':
    input_data = 5
    result = perform_calculation(input_data)
    if result is not None:
        logging.info(f'Result: {result}')
