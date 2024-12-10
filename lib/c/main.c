#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "part1.h"
#include "part2.h"

#define MAX_LENGTH 10000
#define MAX_LINES 1001

int main(int argc, char *argv[]) {
    char *line = (char *)malloc(MAX_LENGTH * sizeof(char));
    char *puzzle_input[MAX_LINES];
    int line_count = 0;

    while (fgets(line, MAX_LENGTH, stdin) != NULL) {
        line[strcspn(line, "\n")] = 0;

        puzzle_input[line_count] = (char *)malloc((strlen(line) + 1) * sizeof(char));
        strcpy(puzzle_input[line_count], line);

        line_count++;
        if (line_count >= MAX_LINES) {
            fprintf(stderr, "Error: Too many lines.\n");
            exit(EXIT_FAILURE);
        }
    }

    line[0] = '\0';
    for (int i = 0; i < line_count; i++) {
        strcat(line, puzzle_input[i]);
        if (i < line_count - 1) {
            strcat(line, "\n");
        }
    }

    if (strcmp("part1", argv[3]) == 0) {
        printf("%s\n", part1(puzzle_input, line_count));
    } else {
        printf("%s\n", part2(puzzle_input, line_count));
    }

    return 0;
}
