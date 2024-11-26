def part2(puzzle_input):
    sequence = puzzle_input[0].split(", ")
    position = [0, 0]
    directions = ["N", "E", "S", "W"]
    direction_index = 0
    visited = set()

    visited.add(tuple(position))

    for instruction in sequence:
        turn = instruction[0]
        distance = int(instruction[1:])

        if turn == "L":
            direction_index = (direction_index - 1) % 4
        elif turn == "R":
            direction_index = (direction_index + 1) % 4

        for _ in range(distance):
            if directions[direction_index] == "N":
                position[1] += 1
            elif directions[direction_index] == "E":
                position[0] += 1
            elif directions[direction_index] == "S":
                position[1] -= 1
            elif directions[direction_index] == "W":
                position[0] -= 1

            if tuple(position) in visited:
                return abs(position[0]) + abs(position[1])

            visited.add(tuple(position))

    return abs(position[0]) + abs(position[1])
