with open('example_file.txt', 'r') as example_file:
    content = example_file.readlines()
    # Process the content line by line or in chunks
    for line in content:
        # Example processing
        print(line.strip())