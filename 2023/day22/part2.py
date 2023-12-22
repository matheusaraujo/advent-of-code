import copy

from helpers import create_space


def part2(puzzle_input):
    bricks, space = create_space(puzzle_input)

    ans = 0

    for brick in bricks:
        ss = dict(space)
        brick.remove(ss)

        for brick2 in copy.deepcopy(bricks):
            if brick.id != brick2.id:
                ans += brick2.slide_down(ss)

    return ans
