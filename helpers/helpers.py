def read_input(file_name = 'input.txt'):
    with open(file_name) as f:
        input = f.readlines()
    return input