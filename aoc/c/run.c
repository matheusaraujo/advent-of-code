#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "part1.h"
#include "part2.h"

#include "puzzle.c"

int run_part1(struct Puzzle puzzle, const char* input);
int run_part2(struct Puzzle puzzle, const char* input);

int main(int argc, char* argv[]) {
    struct Puzzle puzzle = read_puzzle(argv[1]);

    if (!puzzle.initialized) {
        return 1;
    }

    printf("c: Running AoC %s Day %s - %s\n", puzzle.year, puzzle.day, puzzle.title);

    char* input = read_file(puzzle.inputFile);

    if (run_part1(puzzle, input) != 0) {
        return 1;
    }

    if (run_part2(puzzle, input) != 0) {
        return 1;
    }

    free(input);

    return 0;
}

int run_part1(struct Puzzle puzzle, const char* input) {
    int expected_result_part1 = atoi(read_file(puzzle.part1_outputFile));
    clock_t start_time1 = clock();
    int answer1 = part1(input);
    clock_t end_time1 = clock();
    double execution_time1 = ((double)(end_time1 - start_time1)) / CLOCKS_PER_SEC * 1000;

    if (answer1 != expected_result_part1) {
        printf("Part 1 Failed\n%d != %d\n", answer1, expected_result_part1);
        return 1;
    }

    printf("\033[35mPart 1: \033[32m%d\033[3;90m (executed in %.2fms) \033[0m\n", answer1, execution_time1);
    return 0;
}

int run_part2(struct Puzzle puzzle, const char* input) {
    int expected_result_part2 = atoi(read_file(puzzle.part2_outputFile));
    clock_t start_time2 = clock();
    int answer2 = part2(input);
    clock_t end_time2 = clock();
    double execution_time2 = ((double)(end_time2 - start_time2)) / CLOCKS_PER_SEC * 1000;

    if (answer2 != expected_result_part2) {
        printf("Part 2 Failed\n");
        return 1;
    }

    printf("\033[35mPart 2: \033[32m%d\033[3;90m (executed in %.2fms) \033[0m\n", answer2, execution_time2);
    return 0;
}
