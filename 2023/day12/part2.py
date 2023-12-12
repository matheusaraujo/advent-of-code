memory = {}


# a -> springs "???.###"
# b -> groups (1,1,3)
def recursive(a, b):
    if (a, b) in memory:
        return memory[(a, b)]
    ans = 0
    if len(a) == 0:
        # no more springs, groups must be empty to be valid
        ans = 1 if len(b) == 0 else 0
    else:
        if a[0] == ".":
            ans = recursive(a[1:], b)
        elif a[0] == "?":
            ans = recursive("." + a[1:], b) + recursive("#" + a[1:], b)
        elif a[0] == "#":
            if len(b) == 0 or len(a) < sum(b):
                # no more groups or less springs the sum of groups, invalid
                ans = 0
            elif any(c == "." for c in a[0 : b[0]]):
                # there are any "." on next N springs, invalid (N = size of current group)
                ans = 0
            elif len(b) == 1:
                ans = recursive(a[b[0] :], b[1:])
            else:
                if len(a) < b[0] + 1 or a[b[0]] == "#":
                    # less springs than the current group size
                    # or spring just after end of current group is "#", invalid
                    ans = 0
                else:
                    ans = recursive(a[b[0] + 1 :], b[1:])

        memory[(a, b)] = ans

    return ans


def count_arrangement_part2(line):
    [a, b] = line.split(" ")
    a = "?".join([a] * 5)
    b = tuple(int(x) for x in b.split(","))
    b = b * 5
    return recursive(a, b)


def part2(puzzle_input):
    return sum(count_arrangement_part2(line) for line in puzzle_input)
