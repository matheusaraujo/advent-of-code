def define_sequence_value(pattern):
    return int(pattern.replace("#", "1").replace(".", "0"), 2)


def calculate_rows_value(pattern):
    return [define_sequence_value(row) for row in pattern]


def calculate_cols_value(pattern):
    cols = ["".join(row[i] for row in pattern) for i in range(len(pattern[0]))]
    return [define_sequence_value(col) for col in cols]


def calculate_mirror(pattern, is_reflection):
    rows = calculate_rows_value(pattern)
    cols = calculate_cols_value(pattern)

    for i in range(1, max(len(rows), len(cols))):
        if i < len(rows) and is_reflection(rows, i):
            return 100 * i
        if i < len(cols) and is_reflection(cols, i):
            return i

    return 0


def solve(puzzle_input, is_reflection):
    breaks = (
        [-1]
        + [i for i, line in enumerate(puzzle_input) if line == ""]
        + [len(puzzle_input)]
    )
    return sum(
        calculate_mirror(puzzle_input[breaks[i - 1] + 1 : breaks[i]], is_reflection)
        for i in range(1, len(breaks))
    )
