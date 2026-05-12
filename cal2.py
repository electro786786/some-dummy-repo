import logging

logging.basicConfig(level=logging.DEBUG)

def calculate_something(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def main():
    result = calculate_something(10, 2)
    logging.debug('Result: %s', result)

if __name__ == '__main__':
    main()
