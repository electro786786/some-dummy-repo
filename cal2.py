import json

def perform_calculations(data):
    """
    This function performs calculations on the provided data.

    Args:
        data (dict): The data to perform calculations on.

    Returns:
        dict: The calculated results.
    """
    try:
        # Implement the calculation logic here
        results = data['numbers'][0] + data['numbers'][1]
        return {'result': results}
    except Exception as e:
        return {'error': str(e)}


def print_results(data):
    """
    This function prints the results of the calculations.

    Args:
        data (dict): The data to print the results for.
    """
    try:
        results = perform_calculations(data)
        print(json.dumps(results, indent=4))
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    data = {
        'numbers': [10, 20]
    }
    print_results(data)

if __name__ == "__main__":
    main()
