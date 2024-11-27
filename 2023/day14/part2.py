from helpers import count, sort


def map_to_string(matrix):
    return "".join(["".join(map(str, row)) for row in matrix])


def do_cycle(matrix):
    for k in range(4):
        if k == 0:  # north
            for y in range(len(matrix[0])):
                col = "".join([m[y] for m in matrix])
                n_col = sort(col, False)
                for x, _ in enumerate(matrix):
                    matrix[x][y] = n_col[x]
        elif k == 1:  # west
            for x, _ in enumerate(matrix):
                matrix[x] = list(sort("".join(matrix[x]), False))
        elif k == 2:  # south
            for y in range(len(matrix[0])):
                col = "".join([m[y] for m in matrix])
                n_col = sort(col, True)
                for x, _ in enumerate(matrix):
                    matrix[x][y] = n_col[x]
        elif k == 3:  # east
            for x, _ in enumerate(matrix):
                matrix[x] = list(sort("".join(matrix[x]), True))
    return matrix


def part2(puzzle_input, limit=1000000000):
    i, length, memory, matrix = 0, 0, {}, [list(x) for x in puzzle_input]

    while True:
        i = i + 1
        matrix = do_cycle(matrix)
        s = map_to_string(matrix)

        if s in memory:
            length = i - memory[s][0]
            break

        memory[s] = (i, count(matrix))

    index_to_limit = i - length + (limit - i) % length
    return next((v[1] for _, v in memory.items() if v[0] == index_to_limit))
