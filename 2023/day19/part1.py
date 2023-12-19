def read_parts(line):
    pairs = line.strip("{}").split(",")
    return {p.split("=")[0]: int(p.split("=")[1]) for p in pairs}


def read_workflow(line):
    key, parts = line.split("{")
    parts = parts[:-1].split(",")
    r_parts = []
    for part in parts:
        p = part.split(":")
        if len(p) == 1:
            r_parts.append((True, p[0]))
        else:
            r_parts.append((p[0], p[1]))

    return key, r_parts


def evaluate_operation(op, part):
    if op is True:
        return True

    if ">" in op:
        key, value = op.split(">")
        return int(part[key]) > int(value)

    if "<" in op:
        key, value = op.split("<")
        return int(part[key]) < int(value)

    return False


def part1(puzzle_input):
    i_empty = puzzle_input.index("")

    workflows = {}

    for i in range(0, i_empty):
        key, parts = read_workflow(puzzle_input[i])
        workflows[key] = parts

    ans = 0

    for i in range(i_empty + 1, len(puzzle_input)):
        part = read_parts(puzzle_input[i])

        i, w = 0, "in"

        while True:
            operation = workflows[w][i]
            result = evaluate_operation(operation[0], part)

            if result is not True:
                i += 1
            else:
                if operation[1] == "A":
                    ans += sum(part.values())
                    break
                if operation[1] == "R":
                    break
                w = operation[1]
                i = 0

    return ans
