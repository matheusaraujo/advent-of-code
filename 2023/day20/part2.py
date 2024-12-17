# pylint: disable=fixme

import math


# based on https://www.reddit.com/r/adventofcode/comments/18mmfxb/comment/ke5sgxs
# TODO: @matheusaraujo create a graph view of the input
# TODO: @matheusaraujo write the solution explanation
def part2(puzzle_input):
    graph, cycles = {}, []

    for line in puzzle_input:
        source, targets = line.split(" -> ")
        graph[source] = targets.split(", ")

    for m in graph["broadcaster"]:
        m2, _bin = m, ""

        while True:
            g = graph["%" + m2]
            _bin = ("1" if any("&" + n in graph for n in g) else "0") + _bin
            next_l = [n for n in g if "%" + n in graph]
            if len(next_l) == 0:
                break
            m2 = next_l[0]
        cycles += [int(_bin, 2)]

    return math.lcm(*cycles)


### DRAFT
# the input has 4 chains of flip-flops
# those chains are each one connected to a conjunction module (NAND logic)
# that is connected to the final module
#
# inside each chain, each flip-flop toggle at Nth pulse
# the first one toggle at 1th pulse, second at 2nd, third at 4th ...
# so, each chain works as a binary counter
# when all flip-flops on the chain goes to 1, the chain triggers the conjunction
# it will happen on the
# when all chains trigger the conjunction at same time, it will trigger the final module
