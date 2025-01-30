def part1(puzzle_input):
    replacements, input_molecule = parse_input(puzzle_input)
    return len(
        {
            input_molecule[:i] + y + input_molecule[j + 1 :]
            for i in range(len(input_molecule))
            for j in range(i, len(input_molecule))
            if (x := input_molecule[i : j + 1]) in replacements
            for y in replacements[x]
        }
    )


def parse_input(puzzle_input):
    replacements = {}
    for line in puzzle_input[:-2]:
        f, t = line.split(" => ")
        replacements.setdefault(f, []).append(t)
    return replacements, puzzle_input[-1]
