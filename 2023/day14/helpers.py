def sort(line, reverse=False):
    if "#" in line:
        return "#".join(sort(x, reverse) for x in line.split("#"))

    n0 = line.count("O")
    return (
        "".join((len(line) - n0) * ["."] + n0 * ["O"])
        if reverse
        else "".join(n0 * ["O"] + (len(line) - n0) * ["."])
    )


def count(matrix):
    ans, height = 0, len(matrix)
    for row in matrix:
        ans += row.count("O") * height
        height -= 1
    return ans
