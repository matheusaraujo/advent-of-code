import re


def mapping(s, maps):
    for mm in maps:
        for m in mm:
            if m[1] <= s < m[1] + m[2]:
                s = s - (m[1] - m[0])
                break
    return s


def read_input(puzzle_input, problem_version=1):
    def extract_numbers(s):
        return [int(n) for n in re.findall(r"\d+", s)]

    def convert_1d_to_2d(l, cols):
        return [l[i : i + cols] for i in range(0, len(l), cols)]

    puzzle_input = "\n".join(puzzle_input).split(":")

    seeds, maps = extract_numbers(puzzle_input[1]), []
    maps = []

    for i in range(2, 9):
        maps.append(convert_1d_to_2d(extract_numbers(puzzle_input[i]), 3))

    if problem_version == 1:
        seeds.sort()
    else:
        seeds = convert_1d_to_2d(seeds, 2)
        seeds.sort(key=lambda x: x[0])

    return seeds, maps
