from helpers import read_workflows


def read_parts(line):
    pairs = line.strip("{}").split(",")
    return {p.split("=")[0]: int(p.split("=")[1]) for p in pairs}


def evaluate_operation(operation, part):
    if operation is True:
        return True

    if ">" in operation:
        key, value = operation.split(">")
        return int(part[key]) > int(value)

    if "<" in operation:
        key, value = operation.split("<")
        return int(part[key]) < int(value)

    return False


def part1(puzzle_input):
    workflows, i_empty = read_workflows(puzzle_input)
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
