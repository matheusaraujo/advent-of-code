from helpers import create_space


def part1(puzzle_input):
    bricks, space = create_space(puzzle_input)

    for brick in bricks:
        brick.calc_relations(space)

    bricks_to_disintegrate = set()

    for brick in bricks:
        can_disintegrate = True

        for b in brick.supporting:
            bb = next((c for c in bricks if c.id == b), None)
            can_disintegrate = can_disintegrate and len(bb.supported_by) > 1

        if can_disintegrate:
            bricks_to_disintegrate.add(brick.id)

    return len(bricks_to_disintegrate)
