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


def read_workflows(puzzle_input):
    i_empty = puzzle_input.index("")

    workflows = {}

    for i in range(0, i_empty):
        key, parts = read_workflow(puzzle_input[i])
        workflows[key] = parts

    return workflows, i_empty
