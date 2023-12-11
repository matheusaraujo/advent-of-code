def read_input_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        lines = f.readlines()
    return [l.replace("\n", "") for l in lines]


def read_input_file_as_string(file_name):
    with open(file_name, encoding="utf-8") as f:
        lines = f.read()
    return lines
