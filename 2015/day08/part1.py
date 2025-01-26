import re


def get_mem_string(string):
    mem_string = string[1:-1]
    mem_string = mem_string.replace(r"\\", "\\")
    mem_string = mem_string.replace(r"\"", '"')
    mem_string = re.sub(r"\\x[0-9a-fA-F]{2}", "_", mem_string)
    return mem_string


def part1(puzzle_input):
    code_chars, mem_chars = 0, 0

    for string in puzzle_input:
        code_chars += len(string)
        mem_chars += len(get_mem_string(string))

    return code_chars - mem_chars
