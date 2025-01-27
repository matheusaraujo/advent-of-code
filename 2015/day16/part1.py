from helpers import solve


def part1(puzzle_input):
    return solve(
        puzzle_input,
        lambda sue: sue.prop_is("children", 3),
        lambda sue: sue.prop_is("cats", 7),
        lambda sue: sue.prop_is("samoyeds", 2),
        lambda sue: sue.prop_is("pomeranians", 3),
        lambda sue: sue.prop_is("akitas", 0),
        lambda sue: sue.prop_is("vizslas", 0),
        lambda sue: sue.prop_is("goldfish", 5),
        lambda sue: sue.prop_is("trees", 3),
        lambda sue: sue.prop_is("cars", 2),
        lambda sue: sue.prop_is("perfumes", 1),
    )
