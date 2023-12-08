def read_input_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        lines = f.readlines()
    return lines
