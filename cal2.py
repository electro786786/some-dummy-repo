import logging

# Define a function to handle printing messages
def print_message(message):
    logging.info(message)

# Define a function to handle error messages
def print_error(message):
    logging.error(message)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Example usage:
print_message("This is an info message")
print_error("This is an error message")