#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "part1.h"
#include "part2.h"

#include "puzzle.c"

int run(char *part, const char *input, int (*f)(const char *), char *outputFile);

int main(int argc, char *argv[])
{
    struct Puzzle puzzle = read_puzzle(argv[1]);

    if (!puzzle.initialized)
        return 1;

    printf("c: %s\n", puzzle.full_title);

    char *input = read_file(puzzle.inputFile);

    if (run("Part 1", input, part1, puzzle.part1_outputFile))
        return 1;

    if (run("Part 2", input, part2, puzzle.part2_outputFile))
        return 1;

    free(input);

    return 0;
}

int run(char *part, const char *input, int (*f)(const char *), char *outputFile)
{
    int expected_answer = atoi(read_file(outputFile));

    clock_t start_time = clock();
    int received_answer = (*f)(input);
    clock_t end_time = clock();
    double execution_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC * 1000;

    printf("\033[35m%s: \033[32m%d\033[3;90m (executed in %.2fms) \033[0m\n", part, received_answer, execution_time);

    if (expected_answer != received_answer)
    {
        printf("%s Failed - Expected: %d != received: %d\n", part, expected_answer, received_answer);
        return 1;
    }

    return 0;
}
