#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "part1.h"
#include "part2.h"

#include "puzzle.c"

int run(char* part, const char* input, int(*f)(const char*), char* outputFile);

int main(int argc, char* argv[]) {
    struct Puzzle puzzle = read_puzzle(argv[1]);

    if (!puzzle.initialized) {
        return 1;
    }

    printf("c: Running AoC %s Day %s - %s\n", puzzle.year, puzzle.day, puzzle.title);

    char* input = read_file(puzzle.inputFile);

    run("Part 1", input, part1, puzzle.part1_outputFile);
    run("Part 2", input, part2, puzzle.part2_outputFile);

    free(input);

    return 0;
}

int run(char* part, const char* input, int(*f)(const char*), char* outputFile) {
    int expected_answer = atoi(read_file(outputFile));

    clock_t start_time = clock();
    int received_answer = (*f)(input);
    clock_t end_time = clock();
    double execution_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC * 1000;

    if (expected_answer != received_answer) {
        printf("%s Failed - Expected: %d != received: %d\n", part, expected_answer, received_answer);
        return 1;
    }

    printf("\033[35m%s: \033[32m%d\033[3;90m (executed in %.2fms) \033[0m\n", part, received_answer, execution_time);
    return 0;
}
