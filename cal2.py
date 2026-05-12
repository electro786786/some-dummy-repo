try:
    # code that might raise a TypeError
    x = 5 / "a"
except TypeError as e:
    print(f"Invalid input: {e}")