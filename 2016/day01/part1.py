def part1(puzzle_input):
    sequence = puzzle_input[0].split(", ")
    position = [0, 0]
    directions = ["N", "E", "S", "W"]
    direction_index = 0

    for instruction in sequence:
        turn = instruction[0]
        distance = int(instruction[1:])

        if turn == "L":
            direction_index = (direction_index - 1) % 4
        elif turn == "R":
            direction_index = (direction_index + 1) % 4

        if directions[direction_index] == "N":
            position[1] += distance
        elif directions[direction_index] == "E":
            position[0] += distance
        elif directions[direction_index] == "S":
            position[1] -= distance
        elif directions[direction_index] == "W":
            position[0] -= distance

    return abs(position[0]) + abs(position[1])
