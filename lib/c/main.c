#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "part1.h"
#include "part2.h"

#define MAX_LENGTH 10000
#define MAX_LINES 1000

int main(int argc, char *argv[]) {
    char *puzzle_input = (char *)malloc(MAX_LENGTH * sizeof(char));
    char *line[MAX_LINES];
    int line_count = 0;

    while (fgets(puzzle_input, MAX_LENGTH, stdin) != NULL) {
        puzzle_input[strcspn(puzzle_input, "\n")] = 0;

        line[line_count] = (char *)malloc((strlen(puzzle_input) + 1) * sizeof(char));
        strcpy(line[line_count], puzzle_input);

        line_count++;
        if (line_count >= MAX_LINES) {
            fprintf(stderr, "Error: Too many lines.\n");
            exit(EXIT_FAILURE);
        }
    }

    puzzle_input[0] = '\0';
    for (int i = 0; i < line_count; i++) {
        strcat(puzzle_input, line[i]);
        if (i < line_count - 1) {
            strcat(puzzle_input, "\n");
        }
    }

    if (strcmp("part1", argv[3]) == 0) {
        printf("%s\n", part1(puzzle_input));
    } else {
        printf("%s\n", part2(puzzle_input));
    }

    for (int i = 0; i < line_count; i++) {
        free(line[i]);
    }
    free(puzzle_input);

    return 0;
}
