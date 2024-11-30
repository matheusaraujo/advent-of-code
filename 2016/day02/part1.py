def solve(position, moves):
    for move in moves:
        if move == "U" and position > 3:
            position -= 3
        elif move == "D" and position < 7:
            position += 3
        elif move == "L" and position not in [1, 4, 7]:
            position -= 1
        elif move == "R" and position not in [3, 6, 9]:
            position += 1
    return position


def part1(puzzle_input):
    position, result = 5, ""
    for line in puzzle_input:
        position = solve(position, line)
        result += str(position)

    return result
