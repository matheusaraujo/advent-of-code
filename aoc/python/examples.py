import sys

from utils_json import read_puzzle_from_json


def main():
    puzzle = read_puzzle_from_json(sys.argv[1])
    operation = sys.argv[2]
    part = sys.argv[3]
    example = sys.argv[4]

    part = puzzle.part1 if part == "part1" else puzzle.part2

    print(part)


if __name__ == "__main__":
    main()
