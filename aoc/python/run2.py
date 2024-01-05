import sys
import time

part = sys.argv[1]
solutions_dir = sys.argv[2]
puzzle_input = sys.argv[3]

sys.path.append(solutions_dir)

from part1 import part1
from part2 import part2


def run(f):
    start_time = time.time()
    received_answer = f(puzzle_input)
    end_time = time.time()
    execution_time = end_time - start_time
    print(
        f'{{"receivedAnswer": {received_answer}, "executionTime": {(execution_time * 1000):.2f}}}'
    )


def main():
    if part == "part1":
        run(part1)
    elif part == "part2":
        run(part2)


if __name__ == "__main__":
    main()
