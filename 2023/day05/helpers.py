import re

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

def mapping(source, mapping):
    for m in mapping:
        if source >= m[1] and source < m[1] + m[2]:
            return source - (m[1] - m[0])
    return source

def read_input(input):
    def extract_numbers(s):
        return [int(n) for n in re.findall(r'\d+', s)]
    
    input = input.split(':')
    
    seeds, maps = extract_numbers(input[1]), []
    maps = []

    for i in range(2, 9):
        maps.append(convert_1d_to_2d(extract_numbers(input[i]), 3))

    return seeds, maps