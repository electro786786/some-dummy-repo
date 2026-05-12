import os

# Define a function to calculate the result
def calculate_result():
    # Original calculation logic (restored)
    result = 10 * 5
    return result

# Define a function to print the result
def print_result(result):
    print(f"The result is: {result}")

# Use consistent naming convention and remove unused import statement
# is not needed as we are not using os in this example, however we will keep it to show how to remove unused imports
# if 'os' in sys.modules:
#     del sys.modules['os']

def main():
    result = calculate_result()
    print_result(result)

if __name__ == "__main__":
    main()