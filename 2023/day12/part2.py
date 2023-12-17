from functools import lru_cache


def should_keep_checking(springs, groups):
    if len(groups) == 0:
        return False
    if len(springs) < sum(groups):
        return False
    if any(s == "." for s in springs[0 : groups[0]]):
        return False
    if len(groups) > 1 and springs[groups[0]] == "#":
        return False

    return True


# lru_cache is used to memorize solutions based on springs and groups
# previously it was implemented by a homemade solution with a mapping and a wrapper function
@lru_cache
def backtracking(springs, groups):
    if len(springs) == 0:
        return 1 if len(groups) == 0 else 0

    if springs[0] == ".":
        return backtracking(springs[1:], groups)

    if springs[0] == "?":
        return (backtracking("." + springs[1:], groups)) + (
            backtracking("#" + springs[1:], groups)
        )

    if not should_keep_checking(springs, groups):
        return 0

    return (
        (backtracking(springs[groups[0] :], groups[1:]))
        if len(groups) == 1
        else (backtracking(springs[groups[0] + 1 :], groups[1:]))
    )


def count_arrangement_part2(line):
    [springs, groups] = line.split(" ")
    springs = "?".join([springs] * 5)
    groups = tuple(int(x) for x in groups.split(",")) * 5
    return backtracking(springs, groups)


def part2(puzzle_input):
    return sum(count_arrangement_part2(line) for line in puzzle_input)
