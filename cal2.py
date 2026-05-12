import logging

logging.basicConfig(level=logging.INFO)

def calculate_something(a, b):
    if b == 0:
        raise ValueError('b cannot be zero')
    if a == 0:
        raise ValueError('a cannot be zero')
    # rest of the function remains the same

def main():
    a = 10
    b = 20
    try:
        result = calculate_something(a, b)
    except ValueError as e:
        logging.error(f'Error: {e}')
    else:
        logging.info(f'Result: {result}')

if __name__ == '__main__':
    main()
