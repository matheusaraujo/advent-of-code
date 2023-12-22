from dataclasses import dataclass


@dataclass
class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __str__(self):
        return f"({self.x},{self.y}) {self.z}"


@dataclass
class Brick:
    def __init__(self, n, p1: Point, p2: Point):
        self.id = self.__number_to_string(n + 1)
        # forcing p1 < p2, points have only one different dimension
        self.p1 = Point(min(p1.x, p2.x), min(p1.y, p2.y), min(p1.z, p2.z))
        self.p2 = Point(max(p1.x, p2.x), max(p1.y, p2.y), max(p1.z, p2.z))

        self.dir_0 = (
            self.p1.x == self.p2.x and self.p1.y == self.p2.y and self.p1.z == self.p2.z
        )
        self.dir_x = self.p1.x != self.p2.x
        self.dir_y = self.p1.y != self.p2.y
        self.dir_z = self.p1.z != self.p2.z

        self.supporting = []
        self.supported_by = []

    def __str__(self):
        return f"{self.p1} ~ {self.p2}  <- {self.id}"

    def place(self, space):
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                for z in range(self.p1.z, self.p2.z + 1):
                    space[(x, y, z)] = self.id

    def remove(self, space):
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                for z in range(self.p1.z, self.p2.z + 1):
                    space.pop((x, y, z))

    def slide_down(self, space):
        should_slide_down = True
        while should_slide_down:
            if self.p1.z == 1:
                should_slide_down = False
            elif self.dir_z or self.dir_0:
                if (self.p1.x, self.p1.y, self.p1.z - 1) in space:
                    should_slide_down = False
            elif self.dir_x:
                for x in range(self.p1.x, self.p2.x + 1):
                    if (x, self.p1.y, self.p1.z - 1) in space:
                        should_slide_down = False
                        break
            elif self.dir_y:
                for y in range(self.p1.y, self.p2.y + 1):
                    if (self.p1.x, y, self.p1.z - 1) in space:
                        should_slide_down = False
                        break

            if should_slide_down:
                self.__slide_down_z(space)

    def calc_relations(self, space):
        supporting, supported_by = set(), set()
        if self.dir_z or self.dir_0:
            if (self.p1.x, self.p1.y, self.p2.z + 1) in space:
                supporting.add(space[(self.p1.x, self.p1.y, self.p2.z + 1)])
            if (self.p1.x, self.p1.y, self.p1.z - 1) in space:
                supported_by.add(space[(self.p1.x, self.p1.y, self.p1.z - 1)])
        elif self.dir_x:
            for x in range(self.p1.x, self.p2.x + 1):
                if (x, self.p1.y, self.p1.z + 1) in space:
                    supporting.add(space[(x, self.p1.y, self.p1.z + 1)])
                if (x, self.p1.y, self.p1.z - 1) in space:
                    supported_by.add(space[(x, self.p1.y, self.p1.z - 1)])
        elif self.dir_y:
            for y in range(self.p1.y, self.p2.y + 1):
                if (self.p1.x, y, self.p1.z + 1) in space:
                    supporting.add(space[(self.p1.x, y, self.p1.z + 1)])
                if (self.p1.x, y, self.p1.z - 1) in space:
                    supported_by.add(space[(self.p1.x, y, self.p1.z - 1)])

        self.supported_by = list(supported_by)
        self.supporting = list(supporting)

    def __slide_down_z(self, space):
        self.remove(space)
        self.p1.z -= 1
        self.p2.z -= 1
        self.place(space)

    def __number_to_string(self, n):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = ""
        while n > 0:
            remainder = (n - 1) % 26
            result = alphabet[remainder] + result
            n = (n - 1) // 26

        return result
