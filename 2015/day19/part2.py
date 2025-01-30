# based on https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4cu5b/

from random import shuffle


def part2(puzzle_input):
    replacements, target_molecule = parse_input(puzzle_input)
    t, target = 0, target_molecule

    while target != "e":
        tmp = target
        for a, b in replacements:
            if b not in target:
                continue
            target = target.replace(b, a, 1)
            t += 1

        if tmp == target:
            target, t = target_molecule, 0
            shuffle(replacements)

    return t


def parse_input(puzzle_input):
    replacements = []
    for line in puzzle_input[:-2]:
        f, t = line.split(" => ")
        replacements.append((f, t))
    return replacements, puzzle_input[-1]
