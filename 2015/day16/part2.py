from helpers import solve


def part2(puzzle_input):
    return solve(
        puzzle_input,
        lambda sue: sue.prop_is("children", 3),
        lambda sue: sue.prop_is_greater_than("cats", 7),
        lambda sue: sue.prop_is("samoyeds", 2),
        lambda sue: sue.prop_is_less_than("pomeranians", 3),
        lambda sue: sue.prop_is("akitas", 0),
        lambda sue: sue.prop_is("vizslas", 0),
        lambda sue: sue.prop_is_less_than("goldfish", 5),
        lambda sue: sue.prop_is_greater_than("trees", 3),
        lambda sue: sue.prop_is("cars", 2),
        lambda sue: sue.prop_is("perfumes", 1),
    )
