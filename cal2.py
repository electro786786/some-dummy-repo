import logging

# Configure the logger with a level and format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a named logger
logger = logging.getLogger(__name__)

# Define logging functions with error handling
def log_info(message):
    try:
        logger.info(message)
    except Exception as e:
        print(f'Error logging info: {e}')

def log_error(message):
    try:
        logger.error(message)
    except Exception as e:
        print(f'Error logging error: {e}')