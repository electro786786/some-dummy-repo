import logging
from logging.handlers import RotatingFileHandler
import os

# Configure the logger at the module level
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
handler = RotatingFileHandler('printer.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

class Printer:
    def __init__(self):
        pass

    def print(self, message):
        logger.info(message)

def main():
    printer = Printer()
    printer.print("Hello, World!")

if __name__ == "__main__":
    main()