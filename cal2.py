import sys

def print_hello_world_message():
    try:
        print("Hello, World!")
    except Exception as e:
        print(f"An error occurred: {e}")
