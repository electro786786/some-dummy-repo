import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def log_info(message):
    try:
        logging.info(message)
    except logging.exceptions.LoggingError as e:
        print(f'Error logging info: {e}')

def log_error(message):
    try:
        logging.error(message)
    except logging.exceptions.LoggingError as e:
        print(f'Error logging error: {e}')