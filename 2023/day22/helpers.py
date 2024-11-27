from dataclasses import dataclass


@dataclass
class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __str__(self):
        return f"({self.x},{self.y}) {self.z}"


class Brick:
    def __init__(self, n, p1: Point, p2: Point, space):
        self.id = self.__number_to_string(n + 1)
        self.p1 = Point(min(p1.x, p2.x), min(p1.y, p2.y), min(p1.z, p2.z))
        self.p2 = Point(max(p1.x, p2.x), max(p1.y, p2.y), max(p1.z, p2.z))

        self.supporting = set()
        self.supported_by = set()

        self.__place(space)

    def __str__(self):
        return f"{self.p1} ~ {self.p2}  <- {self.id}"

    def slide_down(self, space):
        should_slide_down, count = True, 0

        while should_slide_down:
            should_slide_down = self.p1.z != 1
            for x in range(self.p1.x, self.p2.x + 1):
                for y in range(self.p1.y, self.p2.y + 1):
                    should_slide_down = (
                        should_slide_down and (x, y, self.p1.z - 1) not in space
                    )

            if should_slide_down:
                self.__slide_down_z(space)
                count += 1

        return 1 if count > 0 else 0

    def calc_relations(self, space):
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                if (x, y, self.p2.z + 1) in space:
                    self.supporting.add(space[(x, y, self.p2.z + 1)])
                if (x, y, self.p1.z - 1) in space:
                    self.supported_by.add(space[(x, y, self.p1.z - 1)])

    def __place(self, space):
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                for z in range(self.p1.z, self.p2.z + 1):
                    space[(x, y, z)] = self.id

    def remove(self, space):
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                for z in range(self.p1.z, self.p2.z + 1):
                    space.pop((x, y, z))

    def __slide_down_z(self, space):
        self.remove(space)
        self.p1.z -= 1
        self.p2.z -= 1
        self.__place(space)

    @classmethod
    def __number_to_string(cls, n):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = ""
        while n > 0:
            remainder = (n - 1) % 26
            result = alphabet[remainder] + result
            n = (n - 1) // 26

        return result


def create_space(puzzle_input):
    bricks, space = [], {}

    for idx, line in enumerate(puzzle_input):
        p1, p2 = line.split("~")
        brick = Brick(idx, Point(*p1.split(",")), Point(*p2.split(",")), space)
        bricks.append(brick)

    bricks = sorted(bricks, key=lambda b: b.p1.z)

    for brick in bricks:
        brick.slide_down(space)

    return bricks, space
