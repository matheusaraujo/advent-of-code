from helpers import chunk_array


def part2(puzzle_input, rows, cols):
    layers = chunk_array(list(puzzle_input), cols * rows)

    final_layer = [""] * (rows * cols)

    for i in range(rows * cols):
        for layer in layers:
            if layer[i] in ["0", "1"]:
                final_layer[i] = layer[i]
                break

    return "".join(final_layer).replace("0", "-").replace("1", "#")
