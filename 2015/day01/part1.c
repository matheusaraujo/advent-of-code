#include <stdio.h>

int part1(const char* puzzle_input) {
    int count = 0;

    printf("puzzle_input: %s\n", puzzle_input);

    for(int i = 0; puzzle_input[i] != '\0'; i++)
        count += puzzle_input[i] == '(' ? 1 : -1;

    return count;
}