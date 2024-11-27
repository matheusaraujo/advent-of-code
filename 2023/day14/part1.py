from helpers import count, sort


def part1(puzzle_input):
    matrix = [list(x) for x in puzzle_input]

    for j in range(len(matrix[0])):
        col = "".join([x[j] for x in matrix])
        n_col = sort(col)
        for i, _ in enumerate(matrix):
            matrix[i][j] = n_col[i]

    return count(matrix)
