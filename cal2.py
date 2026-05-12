import sys

def calculate_result(input_value):
    try:
        result = input_value * 2
        return result
    except ValueError:
        print("Invalid input value")
        sys.exit(1)

def main():
    input_value = 5
    result = calculate_result(input_value)
    print(result)

if __name__ == "__main__":
    main()
