#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "part1.h"
#include "part2.h"

#define MAX_LENGTH 10000

int main(int argc, char *argv[]) {
    char *puzzle_input = (char *)malloc(MAX_LENGTH * sizeof(char));
    int line_count = 0;

    while (fgets(puzzle_input, MAX_LENGTH, stdin) != NULL) {
        line_count++;
        puzzle_input[strcspn(puzzle_input, "\n")] = 0;
    }

    if (strcmp("part1", argv[3]) == 0) {
        printf("%s\n", part1(puzzle_input));
    }
    else {
        printf("%s\n", part2(puzzle_input));
    }

    return 0;
}