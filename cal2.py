import logging

# Set logging level to ERROR for sensitive information
logging.basicConfig(level=logging.ERROR)

def calculate_something():
    try:
        # Perform calculation
        result = 1 + 1
        logging.info('Calculation result: %s', result)
    except ZeroDivisionError as e:
        logging.error('Error occurred during calculation: %s', e)
    except Exception as e:
        logging.error('Unknown error occurred during calculation: %s', e)

def main():
    calculate_something()

if __name__ == '__main__':
    main()
