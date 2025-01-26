def get_encoded_str(string):
    encoded_string = '"'
    encoded_string += string.replace("\\", r"\\").replace('"', r"\"")
    encoded_string += '"'
    return encoded_string


def part2(puzzle_input):
    code_chars, encoded_chars = 0, 0

    for s in puzzle_input:
        code_chars += len(s)
        encoded_chars += len(get_encoded_str(s))

    return encoded_chars - code_chars
