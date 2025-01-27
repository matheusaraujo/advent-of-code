import re


class Sue:
    PROPS = [
        "children",
        "cats",
        "samoyeds",
        "pomeranians",
        "akitas",
        "vizslas",
        "goldfish",
        "trees",
        "cars",
        "perfumes",
    ]

    def __init__(self, input_line):
        self.input_line = input_line
        self.sue = re.match(r"Sue (\d+)", self.input_line).groups()[0]
        self.values = {prop: self._extract_property(prop) for prop in self.PROPS}

    def _extract_property(self, prop):
        match = re.search(rf"{prop}: (\d+)", self.input_line)
        return int(match.groups()[0]) if match else None

    def prop_is(self, prop, value):
        return self.values[prop] is None or self.values[prop] == value

    def prop_is_less_than(self, prop, value):
        return self.values[prop] is None or self.values[prop] < value

    def prop_is_greater_than(self, prop, value):
        return self.values[prop] is None or self.values[prop] > value


def solve(puzzle_input, *f_conditions):
    sues = [
        Sue(input_line)
        for input_line in puzzle_input
        if all(f_condition(Sue(input_line)) for f_condition in f_conditions)
    ]
    return sues[0].sue if len(sues) == 1 else None
