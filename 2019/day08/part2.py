from helpers import chunk_array

RLAKF = """
###--#-----##--#--#-####-
#--#-#----#--#-#-#--#----
#--#-#----#--#-##---###--
###--#----####-#-#--#----
#-#--#----#--#-#-#--#----
#--#-####-#--#-#--#-#----
""".replace(
    "\n", ""
)


def part2(puzzle_input, rows=6, cols=25):
    layers = chunk_array(list(puzzle_input[0]), cols * rows)

    final_layer = [""] * (rows * cols)

    for i in range(rows * cols):
        for layer in layers:
            if layer[i] in ["0", "1"]:
                final_layer[i] = layer[i]
                break

    result = "".join(final_layer).replace("0", "-").replace("1", "#")

    for i in range(0, len(result), cols):
        print(result[i : i + cols])

    return "RLAKF" if result == RLAKF else result
