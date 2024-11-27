import sys

from helpers import mapping, read_input


def part2(puzzle_input):
    seeds, maps = read_input(puzzle_input, 2)
    ans = sys.maxsize

    for s in seeds:
        w = 10_000
        lp, rp = s[0], min(s[0] + w, s[0] + s[1] - 1)

        while rp < s[0] + s[1]:
            lpm, rpm = mapping(lp, maps), mapping(rp, maps)

            ans = min(ans, lpm, rpm)

            # if the mapped difference is the same difference as the seeds,
            # we can skip the entire range
            if abs(lpm - rpm) != w:
                for se in range(lp, rp):
                    ans = min(ans, mapping(se, maps))

            lp = rp
            rp = min(rp + w, s[0] + s[1])

    return ans
