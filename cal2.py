import logging

# Set the logging level based on the environment or command-line arguments
logging.basicConfig(level=logging.INFO)

# Rename functions to 'log_info' and 'log_error' for better clarity
def log_info(message):
    try:
        logging.info(message)
    except Exception as e:
        print(f"Error logging info: {e}")

def log_error(message):
    try:
        logging.error(message)
    except Exception as e:
        print(f"Error logging error: {e}")
