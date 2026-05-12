def print_hello_world():
    """Prints Hello, World!"""
    print("Hello, World!")


def main():
    import datetime
    try:
        print_hello_world()
        # Some datetime usage with exception handling
        datetime.datetime.now()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()