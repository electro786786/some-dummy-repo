def print_hello_world(message='Hello, World!'):
    try:
        print(message)
    except Exception as e:
        print(f'An error occurred: {e}')