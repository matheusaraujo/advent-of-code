from helpers import Brick, Point


def part1(puzzle_input):
    bricks, space = [], {}

    for idx, line in enumerate(puzzle_input):
        p1, p2 = line.split("~")
        brick = Brick(idx, Point(*p1.split(",")), Point(*p2.split(",")))
        brick.place(space)
        bricks.append(brick)

    bricks = sorted(bricks, key=lambda b: b.p1.z)

    for brick in bricks:
        brick.slide_down(space)

    bricks = sorted(bricks, key=lambda b: b.p1.z)

    for brick in bricks:
        brick.calc_relations(space)

    bricks_to_disintegrate = set()

    for brick in bricks:
        if len(brick.supporting) == 0:
            bricks_to_disintegrate.add(brick.id)
        else:
            can_disintegrate = True
            for b in brick.supporting:
                bb = next((c for c in bricks if c.id == b), None)
                if len(bb.supported_by) == 1:
                    can_disintegrate = False
            if can_disintegrate:
                bricks_to_disintegrate.add(brick.id)

    return len(bricks_to_disintegrate)
